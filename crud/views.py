from grpc._channel import (
    _InactiveRpcError,
    _MultiThreadedRendezvous,
)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from server.connect_grpc import connect_users_service
from jwt_auth.authentication import CustomJWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from crud.serializers import UserSerializer
from user_proto.user_pb2 import (
    User,
    UserRetrieveRequest,
    UserListRequest,
)
from google.protobuf.json_format import MessageToDict

# Config gRPC to connect gateway service to the user service
stub = connect_users_service()


class UsersList(APIView):
    # Add Authentication class to authenticate user with JWT
    authentication_classes = (CustomJWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    # Serializer class for view
    serializer_class = UserSerializer

    def get(self, request):
        """
        Show List of all users

        :param request:
        :return: List of all users
        """
        try:
            users = stub.List(UserListRequest())
            response = [MessageToDict(user) for user in users]

        except _MultiThreadedRendezvous as e:  # Handle Error while connecting to the server
            return Response({"Error": e.details()}, status=500)

        return Response(response)


class RetrieveUser(APIView):
    # Add Authentication class to authenticate user with JWT
    authentication_classes = (CustomJWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    # Serializer class for view
    serializer_class = UserSerializer

    def get(self, request, pk):
        """
        Get PK from URL then returns the user whose ID is equal to PK

        :param pk: user Primary Key
        :return: User object
        """
        try:
            response = stub.Retrieve(UserRetrieveRequest(id=pk))

        except _InactiveRpcError as e:  # Handle Error while getting user
            code_status = (
                404 if "not found" in e.details() else 500
            )  # get status code from error
            return Response({"Error": e.details()}, status=code_status)

        except _MultiThreadedRendezvous as e:  # Handle Error while connecting to the server
            return Response({"Error": e.details()}, status=500)

        return Response(MessageToDict(response), status=status.HTTP_200_OK)


class CreateUser(APIView):
    # Serializer class for view
    serializer_class = UserSerializer

    def post(self, request):
        """
        Get data from client and pass it to the Users Service
        then create new user

        :param request
        :return: Created User data

        ---
            {
              "username": "string",
              "first_name": "string",
              "last_name": "string",
              "email": "string",
              "password": "string"
            }
        """
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        # Send data to users service
        try:
            user = stub.Create(
                User(
                    username=serializer.data["username"],
                    first_name=serializer.data["first_name"],
                    last_name=serializer.data["last_name"],
                    email=serializer.data["email"],
                    password=serializer.data["password"],
                )
            )

        except _InactiveRpcError as e:  # Handle Error while creating user
            return Response(
                {"Error": e.details()}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        except _MultiThreadedRendezvous as e:  # Handle Error while connecting to the server
            return Response({"Error": e.details()}, status=500)

        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        data = {
            "message": "User created successfully",
            "refresh_token": refresh_token,
            "access_token": access_token,
            "user": MessageToDict(user),
        }

        return Response(
            data,
            status=status.HTTP_201_CREATED,
        )


class UpdateUser(APIView):
    # Add Authentication class to authenticate user with JWT
    authentication_classes = (CustomJWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    # Serializer class for view
    serializer_class = UserSerializer

    def put(self, request, pk):
        """
        Get data from client and pass it to the Users Service
        then update user with passed PK (Primary Key)

        :param request
        :param pk: user primary key
        :return: Updated User data

        ---
            {
              "username": "string",
              "first_name": "string",
              "last_name": "string",
              "email": "string",
              "password": "string"
            }
        """
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # Send data to users service
        try:
            user = stub.Update(
                User(
                    id=pk,
                    username=serializer.data["username"],
                    first_name=serializer.data["first_name"],
                    last_name=serializer.data["last_name"],
                    email=serializer.data["email"],
                    password=serializer.data["password"],
                )
            )

        except _InactiveRpcError as e:  # Handle Error while updating user
            code_status = (
                404 if "not found" in e.details() else 500
            )  # get status code from error
            return Response({"Error": e.details()}, status=code_status)

        except _MultiThreadedRendezvous as e:  # Handle Error while connecting to the server
            return Response({"Error": e.details()}, status=500)

        return Response(
            {"message": "User updated successfully", "detail": MessageToDict(user)},
            status=status.HTTP_200_OK,
        )


class DeleteUser(APIView):
    # Add Authentication class to authenticate user with JWT
    authentication_classes = (CustomJWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        """
        Get primary key from URL and pass it to the Users Service,
        then delete user with passed PK (Primary Key)

        :param request
        :param pk: user primary key
        :return: Deleted User
        """
        # Send data to users service
        try:
            stub.Delete(
                User(
                    id=pk,
                )
            )

        except _InactiveRpcError as e:  # Handle Error while deleting user
            code_status = (
                404 if "not found" in e.details() else 500
            )  # get status code from error
            return Response({"Error": e.details()}, status=code_status)

        except _MultiThreadedRendezvous as e:  # Handle Error while connecting to the server
            return Response({"Error": e.details()}, status=500)

        return Response(
            {
                "message": "User deleted successfully",
            },
            status=status.HTTP_200_OK,
        )

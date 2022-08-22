import grpc
from grpc._channel import (
    _InactiveRpcError,
    _MultiThreadedRendezvous,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from crud.serializers import UserSerializer
from user_proto import user_pb2_grpc
from user_proto.user_pb2 import (
    User,
    UserRetrieveRequest,
    UserListRequest,
)
from google.protobuf.json_format import MessageToDict


# Config gRPC Dev Server to connect gateway service to the user service
channel = grpc.insecure_channel('localhost:50051')
stub = user_pb2_grpc.UserControllerStub(channel)


class UsersList(APIView):
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
            stub.Create(
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

        return Response(
            {"message": "User created successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )


class UpdateUser(APIView):
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
            stub.Update(
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
            {"message": "User updated successfully", "data": serializer.data},
            status=status.HTTP_200_OK,
        )


class DeleteUser(APIView):
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

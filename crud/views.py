import grpc
from grpc._channel import _InactiveRpcError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from crud.serializers import UserSerializer
from user_proto import user_pb2_grpc
from user_proto.user_pb2 import User

# Config gRPC to connect gateway service to the user service
channel = grpc.insecure_channel('localhost:50051')
stub = user_pb2_grpc.UserControllerStub(channel)


class UsersList(APIView):
    def get(self, request):
        return Response({"message": "Test"})


class CreateUser(APIView):
    def post(self, request):
        """
        Get data from client and pass it to the Users Service
        then create new user

        :param request
        :return: Created User data
        """
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # Send data to users service
        try:
            stub.Create(
                User(
                    username=serializer.data['username'],
                    first_name=serializer.data['first_name'], last_name=serializer.data['last_name'],
                    email=serializer.data['email'], password=serializer.data['password'],
                )
            )
        except _InactiveRpcError as e:  # Handle Error while creating user
            return Response({"Error": e.details()}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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
        """
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # Send data to users service
        try:
            stub.Update(
                User(
                    id=pk, username=serializer.data['username'],
                    first_name=serializer.data['first_name'], last_name=serializer.data['last_name'],
                    email=serializer.data['email'], password=serializer.data['password'],
                )
            )
        except _InactiveRpcError as e:  # Handle Error while creating user
            return Response({"Error": e.details()}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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
        except _InactiveRpcError as e:  # Handle Error while creating user
            return Response({"Error": e.details()}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(
            {"message": "User deleted successfully", },
            status=status.HTTP_200_OK,
        )

from grpc._channel import _InactiveRpcError
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import (
    InvalidToken,
    AuthenticationFailed,
)
from rest_framework_simplejwt.settings import api_settings
from server.connect_grpc import connect_users_service
from user_proto.user_pb2 import UserExists

# Config gRPC to connect gateway service to the user service
stub = connect_users_service()


class CustomJWTAuthentication(JWTAuthentication):

    def get_user(self, validated_token):
        try:
            user_id = validated_token[api_settings.USER_ID_CLAIM]
        except KeyError:
            raise InvalidToken("Token contained no recognizable user identification")

        try:
            user = stub.IsUserExists(
                UserExists(
                    id=user_id
                )
            )
        except _InactiveRpcError:
            raise AuthenticationFailed("User not found", code=404)

        return user

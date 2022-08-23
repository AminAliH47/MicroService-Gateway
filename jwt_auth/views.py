from google.protobuf.json_format import MessageToDict
from grpc._channel import _InactiveRpcError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from jwt_auth.serializers import UserLoginSerializer
from server.connect_grpc import connect_users_service
from user_proto.user_pb2 import UserLogin

# Config gRPC to connect gateway service to the user service
stub = connect_users_service()


class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = stub.Login(
                UserLogin(
                    username=serializer.data["username"],
                    password=serializer.data["password"],
                )
            )

        except _InactiveRpcError as e:
            raise AuthenticationFailed(e.details(), code=e.code())

        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        data = {
            "message": "User Logged in successfully.",
            "refresh_token": refresh_token,
            "access_token": access_token,
            "user": MessageToDict(user),
        }

        return Response(data, status=200)

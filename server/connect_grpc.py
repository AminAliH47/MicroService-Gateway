import grpc
from user_proto import user_pb2_grpc


def connect_users_service():
    """
    Create Channel to connect users service

    :return: User controller
    """
    channel = grpc.insecure_channel("10.5.0.1:5000")
    stub = user_pb2_grpc.UserControllerStub(channel)

    return stub

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from user_proto import user_pb2 as user__proto_dot_user__pb2


class UserControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/user_proto.UserController/List',
                request_serializer=user__proto_dot_user__pb2.UserListRequest.SerializeToString,
                response_deserializer=user__proto_dot_user__pb2.User.FromString,
                )
        self.Create = channel.unary_unary(
                '/user_proto.UserController/Create',
                request_serializer=user__proto_dot_user__pb2.User.SerializeToString,
                response_deserializer=user__proto_dot_user__pb2.User.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/user_proto.UserController/Retrieve',
                request_serializer=user__proto_dot_user__pb2.UserRetrieveRequest.SerializeToString,
                response_deserializer=user__proto_dot_user__pb2.User.FromString,
                )
        self.Update = channel.unary_unary(
                '/user_proto.UserController/Update',
                request_serializer=user__proto_dot_user__pb2.User.SerializeToString,
                response_deserializer=user__proto_dot_user__pb2.User.FromString,
                )
        self.Delete = channel.unary_unary(
                '/user_proto.UserController/Delete',
                request_serializer=user__proto_dot_user__pb2.User.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class UserControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=user__proto_dot_user__pb2.UserListRequest.FromString,
                    response_serializer=user__proto_dot_user__pb2.User.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=user__proto_dot_user__pb2.User.FromString,
                    response_serializer=user__proto_dot_user__pb2.User.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=user__proto_dot_user__pb2.UserRetrieveRequest.FromString,
                    response_serializer=user__proto_dot_user__pb2.User.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=user__proto_dot_user__pb2.User.FromString,
                    response_serializer=user__proto_dot_user__pb2.User.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=user__proto_dot_user__pb2.User.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user_proto.UserController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/user_proto.UserController/List',
            user__proto_dot_user__pb2.UserListRequest.SerializeToString,
            user__proto_dot_user__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user_proto.UserController/Create',
            user__proto_dot_user__pb2.User.SerializeToString,
            user__proto_dot_user__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user_proto.UserController/Retrieve',
            user__proto_dot_user__pb2.UserRetrieveRequest.SerializeToString,
            user__proto_dot_user__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user_proto.UserController/Update',
            user__proto_dot_user__pb2.User.SerializeToString,
            user__proto_dot_user__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user_proto.UserController/Delete',
            user__proto_dot_user__pb2.User.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import upf_pb2 as upf__pb2


class UpfStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.plan = channel.unary_unary(
                '/Upf/plan',
                request_serializer=upf__pb2.Problem.SerializeToString,
                response_deserializer=upf__pb2.Answer.FromString,
                )


class UpfServicer(object):
    """Missing associated documentation comment in .proto file."""

    def plan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UpfServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'plan': grpc.unary_unary_rpc_method_handler(
                    servicer.plan,
                    request_deserializer=upf__pb2.Problem.FromString,
                    response_serializer=upf__pb2.Answer.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Upf', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Upf(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def plan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Upf/plan',
            upf__pb2.Problem.SerializeToString,
            upf__pb2.Answer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

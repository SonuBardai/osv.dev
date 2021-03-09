# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from osv import vulnerability_pb2 as osv_dot_vulnerability__pb2
import osv_service_v1_pb2 as osv__service__v1__pb2


class OSVStub(object):
    """Open source vulnerability database.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetVulnById = channel.unary_unary(
                '/osv.v1.OSV/GetVulnById',
                request_serializer=osv__service__v1__pb2.GetVulnByIdParameters.SerializeToString,
                response_deserializer=osv_dot_vulnerability__pb2.Vulnerability.FromString,
                )
        self.QueryAffected = channel.unary_unary(
                '/osv.v1.OSV/QueryAffected',
                request_serializer=osv__service__v1__pb2.QueryAffectedParameters.SerializeToString,
                response_deserializer=osv__service__v1__pb2.VulnerabilityList.FromString,
                )
        self.GetVulnByIdNew = channel.unary_unary(
                '/osv.v1.OSV/GetVulnByIdNew',
                request_serializer=osv__service__v1__pb2.GetVulnByIdParameters.SerializeToString,
                response_deserializer=osv_dot_vulnerability__pb2.Vulnerability.FromString,
                )
        self.QueryAffectedNew = channel.unary_unary(
                '/osv.v1.OSV/QueryAffectedNew',
                request_serializer=osv__service__v1__pb2.QueryAffectedParameters.SerializeToString,
                response_deserializer=osv__service__v1__pb2.VulnerabilityList.FromString,
                )


class OSVServicer(object):
    """Open source vulnerability database.
    """

    def GetVulnById(self, request, context):
        """Return a `Vulnerability` object for a given OSV ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryAffected(self, request, context):
        """Query vulnerabilities for a particular project at a given commit or
        version.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVulnByIdNew(self, request, context):
        """Return a `Vulnerability` object for a given OSV ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryAffectedNew(self, request, context):
        """Query vulnerabilities for a particular project at a given commit or
        version.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OSVServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetVulnById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVulnById,
                    request_deserializer=osv__service__v1__pb2.GetVulnByIdParameters.FromString,
                    response_serializer=osv_dot_vulnerability__pb2.Vulnerability.SerializeToString,
            ),
            'QueryAffected': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryAffected,
                    request_deserializer=osv__service__v1__pb2.QueryAffectedParameters.FromString,
                    response_serializer=osv__service__v1__pb2.VulnerabilityList.SerializeToString,
            ),
            'GetVulnByIdNew': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVulnByIdNew,
                    request_deserializer=osv__service__v1__pb2.GetVulnByIdParameters.FromString,
                    response_serializer=osv_dot_vulnerability__pb2.Vulnerability.SerializeToString,
            ),
            'QueryAffectedNew': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryAffectedNew,
                    request_deserializer=osv__service__v1__pb2.QueryAffectedParameters.FromString,
                    response_serializer=osv__service__v1__pb2.VulnerabilityList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'osv.v1.OSV', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OSV(object):
    """Open source vulnerability database.
    """

    @staticmethod
    def GetVulnById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osv.v1.OSV/GetVulnById',
            osv__service__v1__pb2.GetVulnByIdParameters.SerializeToString,
            osv_dot_vulnerability__pb2.Vulnerability.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryAffected(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osv.v1.OSV/QueryAffected',
            osv__service__v1__pb2.QueryAffectedParameters.SerializeToString,
            osv__service__v1__pb2.VulnerabilityList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVulnByIdNew(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osv.v1.OSV/GetVulnByIdNew',
            osv__service__v1__pb2.GetVulnByIdParameters.SerializeToString,
            osv_dot_vulnerability__pb2.Vulnerability.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryAffectedNew(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osv.v1.OSV/QueryAffectedNew',
            osv__service__v1__pb2.QueryAffectedParameters.SerializeToString,
            osv__service__v1__pb2.VulnerabilityList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

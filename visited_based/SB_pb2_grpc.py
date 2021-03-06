# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import SB_pb2 as SB__pb2


class SimilarityRecomStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AdRecom = channel.unary_unary(
        '/SimilarityRecom/AdRecom',
        request_serializer=SB__pb2.PId.SerializeToString,
        response_deserializer=SB__pb2.PriorityIds.FromString,
        )
    self.PostRecom = channel.unary_unary(
        '/SimilarityRecom/PostRecom',
        request_serializer=SB__pb2.PId.SerializeToString,
        response_deserializer=SB__pb2.PriorityIds.FromString,
        )


class SimilarityRecomServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def AdRecom(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PostRecom(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SimilarityRecomServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AdRecom': grpc.unary_unary_rpc_method_handler(
          servicer.AdRecom,
          request_deserializer=SB__pb2.PId.FromString,
          response_serializer=SB__pb2.PriorityIds.SerializeToString,
      ),
      'PostRecom': grpc.unary_unary_rpc_method_handler(
          servicer.PostRecom,
          request_deserializer=SB__pb2.PId.FromString,
          response_serializer=SB__pb2.PriorityIds.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'SimilarityRecom', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

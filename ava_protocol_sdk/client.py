import grpc
from .avsproto import avs_pb2, avs_pb2_grpc

class AggregatorClient:
    def __init__(self, endpoint: str):
        self.channel = grpc.insecure_channel(endpoint)
        self.stub = avs_pb2_grpc.AggregatorStub(self.channel)


    def get_smart_account_address(self, owner: str) -> dict:
        request = avs_pb2.AddressRequest(owner=owner)
        try:
            response = self.stub.GetSmartAccountAddress(request)
            return {
                    "smart_account_address": response.smart_account_address,
                    "nonce" : response.nonce
            }
        except grpc.RpcError as e:
            raise Exception(f"gRPC Error: {e.code()} - {e.details()}") from e

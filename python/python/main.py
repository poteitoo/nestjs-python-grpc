from concurrent.futures import ThreadPoolExecutor
import grpc
from autogen.sample_pb2 import SampleData, SampleDataById
from autogen.sample_pb2_grpc import (
    add_AppServiceServicer_to_server,
    AppServiceServicer,
)


# レスポンスの処理
class Greeter(AppServiceServicer):
    def FindOne(self, request: SampleDataById, context):
        print('request', request.id)
        print('context', context)
        return SampleData(id=1, name='poepoeee')


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_AppServiceServicer_to_server(Greeter(), server)

    # サーバーの立ち上げ
    server.add_insecure_port("[::]:5001")
    server.start()
    print("server started")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

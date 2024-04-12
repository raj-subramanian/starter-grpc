import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    # Create a channel to connect to the server.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        # Prepare the request
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='World'))
        print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()

# starter-grpc

A simple Starter project for gRPC

Pre-requisites:
> - pip or conda install grpcio-tools
> - pip or conda install grpcio

Use the proto file to create the code:
> - python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. helloworld.proto

To run:
> - python greeter_server.py
> - python greeter_client.py in a separate terminal

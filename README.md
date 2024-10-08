This is a Python SDK which allows you to interact with some basic Ava Protocol Ethereum functions like creating "tasks" and automating smart contract deployment.



# Special Notes

For some reason, the latest versions of grpcio and grpcio-tools you install from pip are .28, but it comes bundled with proto .27, so when you generate python code from a .proto file, it will be incompatible with its own runtime. To fix this, download the latest release of protoc from its github page, put it in /usr/local/bin, and then use a special flag to pass a path to a protoc installation: `python3 -m grpc_tools.protoc --proto_path=<path_to_proto_files> --python_out=<output_directory> --grpc_python_out=<output_directory> --plugin=protoc-gen-grpc_python=/usr/local/bin/protoc <your_proto_file.proto>`

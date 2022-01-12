# Copyright 2022 Franklin Selva. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from concurrent import futures

import grpc
from upf.shortcuts import *

import upf_pb2_grpc as upf_pb2_grpc
from from_protobuf import FromProtobufConverter
from problem import get_example_problems
from to_protobuf import ToProtobufConverter

EXPORT_TEMPLATE = False


class UpfGrpcServer(upf_pb2_grpc.UpfServicer):
    def __init__(self, port):
        self.server = None
        self.port = port
        self.from_protobuf = FromProtobufConverter()
        self.to_protobuf = ToProtobufConverter()

    def plan(self, request, context):
        problem = self.from_protobuf.convert(request)

        with OneshotPlanner(name="tamer", params={"weight": 0.8}) as planner:
            plan = planner.solve(problem)
            answer = self.to_protobuf.convert(plan)
            return answer
        return None

    def start(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        upf_pb2_grpc.add_UpfServicer_to_server(self, self.server)
        self.server.add_insecure_port("0.0.0.0:%d" % self.port)
        self.server.start()

    def wait_for_termination(self):
        self.server.wait_for_termination()


class UpfGrpcClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.from_protobuf = FromProtobufConverter()
        self.to_protobuf = ToProtobufConverter()

    def __call__(self, problem):
        with grpc.insecure_channel("%s:%d" % (self.host, self.port)) as channel:
            stub = upf_pb2_grpc.UpfStub(channel)
            req = self.to_protobuf.convert(problem)

            if EXPORT_TEMPLATE:
                with open("data/UPF.md", "w") as f:
                    f.write("```bash\n" + str(req) + "```")

            answer = stub.plan(req)

            r = self.from_protobuf.convert(answer, problem)
            return r


def main():
    """Main function"""
    # Setup problem
    print("\033[92m" + "Acquiring problems..." + "\033[0m")
    problems_ = get_example_problems()
    print("\033[94m" + "Acquired problems: " + "\033[0m")
    for key in problems_.keys():
        print(key)
    problem = problems_["robot"].problem

    if EXPORT_TEMPLATE:
        with open("data/problem.md", "w") as f:
            f.write("```bash\n" + str(problem) + "```")

    # Start server
    print("\n\033[92m" + "Starting server..." + "\033[0m")
    server = UpfGrpcServer(port=2222)
    server.start()

    # Start client
    print("\033[92m" + "Starting client..." + "\033[0m")
    client = UpfGrpcClient(host="localhost", port=2222)
    plan = client(problem)
    with PlanValidator(problem_kind=problem.kind()) as validator:
        res = validator.validate(problem, plan)
        print(res)

    server.wait_for_termination()


if __name__ == "__main__":
    main()

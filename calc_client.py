from concurrent import futures
import time

import grpc

import calc_pb2
import calc_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50053")
    stub = calc_pb2_grpc.CalculatorStub(channel)

    response = stub.Add(calc_pb2.AddRequest(n1 = 20, n2 = 10))
    print(response.n1)

if __name__ =='__main__':
    run()
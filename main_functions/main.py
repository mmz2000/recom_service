import SB_pb2_grpc
import SB_pb2
import grpc
import threading
from concurrent import futures


channel1 = grpc.insecure_channel('localhost:7000')
channel2 = grpc.insecure_channel('localhost:8000')
stub1 = SB_pb2_grpc.SimilarityRecomStub(channel=channel1)
stub2 = SB_pb2_grpc.SimilarityRecomStub(channel=channel2)

def Ad_recom (pid):
    result1 = None
    result2 = None
    ad_rates = {}
    with futures.ThreadPoolExecutor() as executor:
        t1 = executor.submit(stub1.AdRecom, SB_pb2.PId(id=pid))
        t2 = executor.submit(stub2.AdRecom, SB_pb2.PId(id=pid))
        result1 = t1.result()
        result2 = t2.result()
    for i in result1.ids:
        ad_rates[i.id] = i.value
    for i in result2.ids:
        if i.id in ad_rates.keys():
            ad_rates[i.id] += i.value
        else:
            ad_rates[i.id] = i.value
    return [k for k, v in sorted(ad_rates.items(), key=lambda item: item[1])]


def Post_recom(pid):
    result1 = None
    result2 = None
    post_rates = {}
    with futures.ThreadPoolExecutor() as executor:
        t1 = executor.submit(stub1.PostRecom,  SB_pb2.PId(id=pid))
        t2 = executor.submit(stub2.PostRecom,  SB_pb2.PId(id=pid))
        result1 = t1.result()
        result2 = t2.result()
    for i in result1.ids:
        post_rates[i.id] = i.value
    for i in result2.ids:
        if i.id in post_rates.keys():
            post_rates[i.id] += i.value
        else:
            post_rates[i.id] = i.value
    return [k for k, v in sorted(post_rates.items(), key=lambda item: item[1])]

if __name__ == "__main__":
    while True:
        pid = input("enter user id:")
        print(Ad_recom(pid))
        print(Post_recom(pid))

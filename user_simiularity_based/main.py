from concurrent import futures
import db_pb2_grpc
import db_pb2
import SB_pb2_grpc
import SB_pb2
import grpc


class SimilarityRecom(SB_pb2_grpc.SimilarityRecomServicer):
    def __init__(self):
        channel = grpc.insecure_channel('localhost:5000')
        self.stub = db_pb2_grpc.dbhandleStub(channel=channel)

    def AdRecom(self, request, context):
        return AD(request.id, self.stub)

    def PostRecom(self, request, context):
        return PR(request.id, self.stub)


def AD(id, stub):
    Ad_rating = {}
    profile_data = stub.UserIdtoData(id)
    all_posts = list(profile_data.viewed_post_id) + \
        list(profile_data.liked_post_id)
    ads = list(profile_data.clicked_ad_id)
    users = User_digger(all_posts, ads, stub)
    for i in users:
        temp = stub.UserIdtoData(i)
        similarity_rate = similarity(profile_data, temp, True)
        for j in temp.clicked_ad_id:
            if j not in profile_data.clicked_ad_id:
                if j in list(Ad_rating.keys()):
                    Ad_rating[j] += similarity_rate
                else:
                    Ad_rating[j] = similarity_rate
    result = SB_pb2.PriorityIds()
    for i in Ad_rating.keys():
        result.ids.append(SB_pb2.touples(id=i, value=Ad_rating[i]))
    return result


def PR(id, stub):
    post_rating = {}
    profile_data = stub.UserIdtoData(id)
    all_posts = list(profile_data.viewed_post_id) + \
        list(profile_data.liked_post_id)
    ads = list(profile_data.clicked_ad_id)
    users = User_digger(all_posts, ads, stub)
    for i in users:
        temp = stub.UserIdtoData(i)
        similarity_rate = similarity(profile_data, temp, False)
        temp_posts = list(temp.viewed_post_id) + list(temp.liked_post_id)
        for j in temp_posts:
            if j not in all_posts:
                if j in list(post_rating.keys()):
                    post_rating[j] += similarity_rate
                else:
                    post_rating[j] = similarity_rate
    result = SB_pb2.PriorityIds()
    for i in post_rating.keys():
        result.ids.append(SB_pb2.touples(id=i, value=post_rating[i]))
    return result


def User_digger(posts, ads, stub):
    users = []
    for i in posts:
        p_data = stub.PostIdToData(i)
        for j in p_data.viewers_id:
            if j not in users:
                users.append(j)
        for k in p_data.likers_id:
            if k not in users:
                users.append(k)
    for l in ads:
        ad_data = stub.AdIdToData(l)
        for k in ad_data.clickers_id:
            users.append(l)
    return users


def similarity(data, profile_data, flag):
    clicked_rate = len(set(data.clicked_ad_id).intersection(
        set(profile_data.clicked_ad_id)))/len(set(data.clicked_ad_id))
    viewed_rate = len(set(data.viewed_post_id).intersection(
        set(profile_data.viewed_post_id)))/len(set(data.viewed_post_id))
    liked_rate = len(set(data.liked_ad_id).intersection(
        set(profile_data.liked_ad_id)))/len(set(data.liked_ad_id))
    if flag:
        return (liked_rate*3 + viewed_rate*2 + clicked_rate*2)/7
    else:
        return (liked_rate*3 + viewed_rate*2 + clicked_rate*1)/6


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    SB_pb2_grpc.add_SimilarityRecomServicer_to_server(
        SimilarityRecom(), server)
    server.add_insecure_port("[::]:8000")
    server.start()
    try:
        print("for stopping the server : Ctrl+c")
        while True:
            pass
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)


if __name__ == "__main__":
    serve()

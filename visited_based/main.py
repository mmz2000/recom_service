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


def AD(pid, stub):
    tags_rate = {}
    publisher_rate = {}
    ad_ratings = {}
    profile_data = stub.UserIdtoData(db_pb2.Id(id=pid))
    for i in profile_data.clicked_ad_id:
        A_data = stub.AdIdToData(db_pb2.Id(id=i))
        for j in A_data.tags:
            if j in tags_rate.keys():
                tags_rate[j] += 2/len(list(profile_data.clicked_ad_id))
            else:
                tags_rate[j] = 2/len(list(profile_data.clicked_ad_id))
        if A_data.publisher_id in publisher_rate.keys():
            publisher_rate[A_data.publisher_id] += 6 / \
                len(list(profile_data.clicked_ad_id))
        else:
            publisher_rate[A_data.publisher_id] = 6 / \
                len(list(profile_data.clicked_ad_id))
    for i in profile_data.viewed_post_id:
        P_data = stub.PostIdtoData(db_pb2.Id(id=i))
        for j in P_data.tags:
            if j in tags_rate.keys():
                tags_rate[j] += 2/len(list(profile_data.viewed_post_id))
            else:
                tags_rate[j] = 2/len(list(profile_data.viewed_post_id))
        if P_data.publisher_id in publisher_rate.keys():
            publisher_rate[P_data.publisher_id] += 6 / \
                len(list(profile_data.viewed_post_id))
        else:
            publisher_rate[P_data.publisher_id] = 6 / \
                len(list(profile_data.viewed_post_id))
    for i in profile_data.liked_post_id:
        P_data = stub.PostIdtoData(db_pb2.Id(id=i))
        for j in P_data.tags:
            if j in tags_rate.keys():
                tags_rate[j] += 3/len(list(profile_data.liked_post_id))
            else:
                tags_rate[j] = 3/len(list(profile_data.liked_post_id))
        if P_data.publisher_id in publisher_rate.keys():
            publisher_rate[P_data.publisher_id] += 9 / \
                len(list(profile_data.liked_post_id))
        else:
            publisher_rate[P_data.publisher_id] = 9 / \
                len(list(profile_data.liked_post_id))
    for i in tags_rate.keys():
        temp = stub.TagToAd(db_pb2.Id(id=i))
        for j in temp.ads_id:
            if j not in profile_data.clicked_ad_id:
                if j in ad_ratings.keys():
                    ad_ratings[j] += tags_rate[i]
                else:
                    ad_ratings[j] = tags_rate[i]
    for i in publisher_rate.keys():
        temp = stub.AuthorToAd(db_pb2.Id(id=i))
        for j in temp.ads_id:
            if j not in profile_data.clicked_ad_id:
                if j in ad_ratings.keys():
                    ad_ratings[j] += publisher_rate[i]
                else:
                    ad_ratings[j] = publisher_rate[i]
    result = SB_pb2.PriorityIds()
    for i in ad_ratings.keys():
        result.ids.append(SB_pb2.touples(id=i, value=ad_ratings[i]))
    return result


def PR(pid, stub):
    tags_rate = {}
    publisher_rate = {}
    post_ratings = {}
    profile_data = stub.UserIdtoData(db_pb2.Id(id=pid))
    for i in profile_data.clicked_ad_id:
        A_data = stub.AdIdToData(db_pb2.Id(id=i))
        for j in A_data.tags:
            if j in tags_rate.keys():
                tags_rate[j] += 1/len(list(profile_data.clicked_ad_id))
            else:
                tags_rate[j] = 1/len(list(profile_data.clicked_ad_id))
        if A_data.publisher_id in publisher_rate.keys():
            publisher_rate[A_data.publisher_id] += 3 / \
                len(list(profile_data.clicked_ad_id))
        else:
            publisher_rate[A_data.publisher_id] = 3 / \
                len(list(profile_data.clicked_ad_id))
    for i in profile_data.viewed_post_id:
        P_data = stub.PostIdtoData(db_pb2.Id(id=i))
        for j in P_data.tags:
            if j in tags_rate.keys():
                tags_rate[j] += 2/len(list(profile_data.viewed_post_id))
            else:
                tags_rate[j] = 2/len(list(profile_data.viewed_post_id))
        if P_data.publisher_id in publisher_rate.keys():
            publisher_rate[P_data.publisher_id] += 6 / \
                len(list(profile_data.viewed_post_id))
        else:
            publisher_rate[P_data.publisher_id] = 6 / \
                len(list(profile_data.viewed_post_id))
    for i in profile_data.liked_post_id:
        P_data = stub.PostIdtoData(db_pb2.Id(id=i))
        for j in P_data.tags:
            if j in tags_rate.keys():
                tags_rate[j] += 3/len(list(profile_data.liked_post_id))
            else:
                tags_rate[j] = 3/len(list(profile_data.liked_post_id))
        if P_data.publisher_id in publisher_rate.keys():
            publisher_rate[P_data.publisher_id] += 8 / \
                len(list(profile_data.liked_post_id))
        else:
            publisher_rate[P_data.publisher_id] = 8 / \
                len(list(profile_data.liked_post_id))
    for i in tags_rate.keys():
        temp = stub.TagToPost(db_pb2.Id(id=i))
        for j in temp.posts_id:
            if j not in profile_data.viewed_post_id:
                if j in post_ratings.keys():
                    post_ratings[j] += tags_rate[i]
                else:
                    post_ratings[j] = tags_rate[i]
    for i in publisher_rate.keys():
        temp = stub.AuthorToPosts(db_pb2.Id(id=i))
        for j in temp.posts_id:
            if j not in profile_data.viewed_post_id:
                if j in post_ratings.keys():
                    post_ratings[j] += publisher_rate[i]
                else:
                    post_ratings[j] = publisher_rate[i]
    result = SB_pb2.PriorityIds()
    for i in post_ratings.keys():
        result.ids.append(SB_pb2.touples(id=i, value=post_ratings[i]))
    return result


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    SB_pb2_grpc.add_SimilarityRecomServicer_to_server(
        SimilarityRecom(), server)
    server.add_insecure_port("[::]:7000")
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

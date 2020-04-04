from concurrent import futures
import db_pb2_grpc
import db_pb2
import grpc
import json


class dbhandleServicer(db_pb2_grpc.dbhandleServicer):
    def __init__(self):
        self.db = json.load(open("db.json"))

    def AdIdToData(self, request, context):
        obj = self.db["Ads"][request.id]
        if obj != None:
            return db_pb2.AdData(tags=obj["tags"], clickers_id=obj["clickers_id"], pub_date=obj["pub_date"], publisher_id=obj["publisher_id"])
        else:
            return db_pb2.AdData(tags=[], clickers_id=[], pub_date="", publisher_id="")

    def PostIdtoData(self, request, context):
        obj = self.db["Posts"][request.id]
        if obj != None:
            return db_pb2.PostData(tags=obj["tags"], viewers_id=obj["viewers_id"], likers_id=obj["likers_id"], pub_date=obj["pub_date"], publisher_id=obj["publisher_id"])
        else:
            return db_pb2.PostData(tags=[], viewers_id=[], likers_id=[], pub_date="", publisher_id="")

    def UserIdtoData(self, request, context):
        obj = self.db["Users"][request.id]
        if obj != None:
            return db_pb2.UserData(clicked_ad_id=obj["clicked_ad_id"], viewed_post_id=obj["viewed_post_id"], liked_post_id=obj["liked_post_id"])
        else:
            return db_pb2.UserData(clicked_ad_id=[], viewed_post_id=[], liked_post_id=[])

    def AuthorToAd(self, request, context):
        tag = request.id
        obj = self.db["Ads"]
        ads = []
        for k in obj.keys():
            if tag == obj[k]["publisher_id"]:
                ads.append(k)
        return db_pb2.Ads(ads_id=ads)

    def TagToAd(self, request, context):
        tag = request.tag
        obj = self.db["Ads"]
        ads = []
        for k in obj.keys():
            if tag in obj[k]["tags"]:
                ads.append(k)
        return db_pb2.Ads(ads_id=ads)

    def TagToPost(self, request, context):
        tag = request.tag
        obj = self.db["Posts"]
        posts = []
        for k in obj.keys():
            if tag in obj[k]["tags"]:
                posts.append(k)
        return db_pb2.Posts(posts_id=posts)

    def AuthorToPosts(self, request, context):
        tag = request.id
        obj = self.db["Posts"]
        posts = []
        for k in obj.keys():
            if tag == obj[k]["publisher_id"]:
                posts.append(k)
        return db_pb2.Posts(posts_id=posts)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    db_pb2_grpc.add_dbhandleServicer_to_server(dbhandleServicer(), server)
    server.add_insecure_port("[::]:5000")
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

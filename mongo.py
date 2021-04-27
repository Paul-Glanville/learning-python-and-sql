import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "MyFirstDB"
COLLECTION = "celebrities"


def mongo_correct(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB")


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

coll.update_many(
    {"nationality": "american"},
    {"$set": {"hair_color": "maroon"}}
)

documents = coll.find()

for doc in documents:
    print(doc)

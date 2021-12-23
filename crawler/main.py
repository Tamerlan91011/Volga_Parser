from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

db = client['test']

collection = db['users']

for doc in collection.find():
    print(doc)

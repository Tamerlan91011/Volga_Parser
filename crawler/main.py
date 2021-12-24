from pymongo import MongoClient
from parser import parse
import json

client = MongoClient('mongodb://localhost:27017/')

db = client['test']

collection = db['news']

news = parse(5)

for new in news:
    link = new['link']
    try:
        collection.insert_one(new)
    except Exception:
        print(f'Новость "{link}" в базе уже есть!')


for doc in collection.find():
    print(doc)


import pymongo
import os

client = pymongo.MongoClient(os.getenv('MONGO_ADDRESS'))
client = client[os.getenv('DATABASE')]



from database import Database
from models.post import Post

__author__ = "jbarry1506"

Database.initialize()

post = Post()

"""
import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['bodyVaultWeb']
collection = database['users']

users = [user for user in collection.find({})]

print(users)

"""
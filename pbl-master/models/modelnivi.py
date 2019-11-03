from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client['nivi']

def create_user(user_info):
	db['users'].insert_one(user_info)
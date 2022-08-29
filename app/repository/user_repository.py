from bson import ObjectId
from flask_pymongo import PyMongo
from pymongo.collection import Collection


class UserRepository:
    def __init__(self, db: PyMongo):
        self.db = db

    def find(self, id):
        return self.db.users.find_one({
            '_id': ObjectId(id)
        })

    def find_one_by_username(self, username: str) -> Collection:
        user = self.db.users.find_one({
            'username': username
        })

        return user


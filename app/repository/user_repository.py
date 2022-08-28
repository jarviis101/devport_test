from flask_pymongo import PyMongo
from pymongo.collection import Collection


class UserRepository:
    def __init__(self, db: PyMongo):
        self.db = db

    def findOneByUsername(self, username: str) -> Collection:
        user = self.db.users.find_one({
            'username': username
        })

        return user

    def findAll(self) -> Collection:
        return self.db.users.find()


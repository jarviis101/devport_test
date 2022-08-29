from bson import ObjectId
from flask_pymongo import PyMongo

from app.dto.user.update_password_dto import UpdatePasswordDTO
from app.model.user import User
from app.repository.user_repository import UserRepository


class UserService:
    def __init__(self, db: PyMongo):
        self.db = db
        self.userRepository = UserRepository(db)

    def password_update(self, dto: UpdatePasswordDTO, auth_user: User) -> None:
        self.db.users.find_one_and_update({'_id': auth_user.id}, {
            "$set": {
                'password': dto.get_password()
            }
        })

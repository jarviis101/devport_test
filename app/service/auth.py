import json
import bson.json_util
import flask_login
import pymongo
from flask_pymongo import PyMongo
from werkzeug.security import check_password_hash

from app.dto.auth.login_dto import LoginDTO
from app.dto.auth.register_dto import RegisterDTO, RegisterDTOEncoder
from app.exception.auth.user_register_validation_exception import UserRegisterValidationException
from app.model.user import User
from app.repository.user_repository import UserRepository


class RegisterService:
    def __init__(self, db: PyMongo):
        self.db = db
        # TODO: i think this part of code must have to execute a once time, maybe trough migrations
        self.db.users.create_index([('username', pymongo.ASCENDING)], unique=True)

    def register(self, dto: RegisterDTO) -> None:
        user = json.dumps(dto, cls=RegisterDTOEncoder)
        self.db.users.insert_one(
            bson.json_util.loads(user)
        )


class LoginService:
    def __init__(self, db: PyMongo):
        self.userRepository = UserRepository(db)
        self.db = db

    def login(self, dto: LoginDTO) -> None:
        user = self.userRepository.find_one_by_username(dto.get_username())

        if not user or not check_password_hash(user['password'], dto.get_password()):
            raise UserRegisterValidationException('Invalid credentials')

        auth_user = User()
        auth_user.id = user['_id']

        flask_login.login_user(auth_user)

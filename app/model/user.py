from flask import Request
from flask_login import UserMixin

from app import login_manager
from app.repository.user_repository import UserRepository
from app import client

repository = UserRepository(client.db)


class User(UserMixin):
    pass


@login_manager.user_loader
def user_loader(username: str):
    user = repository.findOneByUsername(username)
    if not user:
        return

    auth_user = User()
    auth_user.id = user['username']
    return auth_user


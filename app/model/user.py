from typing import Optional

from flask_login import UserMixin

from app import login_manager
from app.repository.user_repository import UserRepository
from app import client

repository = UserRepository(client.db)


class User(UserMixin):
    pass


@login_manager.user_loader
def user_loader(identifier: str) -> Optional[User]:
    user = repository.find(identifier)
    if not user:
        return

    auth_user = User()
    auth_user.id = user['_id']
    auth_user.username = user['username']
    return auth_user


@login_manager.request_loader
def request_loader(request):
    # TODO: Create for JWT auth
    pass

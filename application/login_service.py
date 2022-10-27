from dependency_injector.wiring import Provide, inject
from infrastructure.injector import Injector
from domain.interfaces.user_repository import UserRepository


class LoginService:

    @inject
    def __init__(self, user_repository: UserRepository = Provide[Injector.user_repo]):
        self.user_repository = user_repository

    def authenticate_user(self, username: str, password: str):
        user = self.user_repository.get_by_username(username)
        user.verify_password(password)
        return user

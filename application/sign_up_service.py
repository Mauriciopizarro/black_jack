from dependency_injector.wiring import Provide, inject
from domain.user import UserPlainPassword
from infrastructure.injector import Injector
from domain.interfaces.user_repository import UserRepository
from application.token_service import TokenService


class SignUpService:

    @inject
    def __init__(self, user_repository: UserRepository = Provide[Injector.user_repo]):
        self.user_repository = user_repository

    def sign_up(self, username, plain_password):
        user = UserPlainPassword(username=username, plain_password=plain_password)
        user_response = self.user_repository.save_user(user)
        token = TokenService.generate_token(user_response)
        return {
            "token": token,
            "username": user_response.username,
            "user_id": user_response.id,
        }


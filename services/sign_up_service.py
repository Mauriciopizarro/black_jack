from models.user import UserPlainPassword
from repositories.user_pyson_repository import UserPysonRepository
from services.token_service import TokenService


class SignUpService:
    def __init__(self):
        self.user_repository = UserPysonRepository.get_instance()

    def sign_up(self, username, plain_password):
        user = UserPlainPassword(username=username, plain_password=plain_password)
        user_response = self.user_repository.save_user(user)
        token = TokenService.generate_token(user_response)
        return {
            "token": token,
            "username": user_response.username,
            "user_id": user_response.id,
        }


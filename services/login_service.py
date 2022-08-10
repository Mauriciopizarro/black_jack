from repositories.user_repository import UserRepository


class LoginService:

    def __init__(self):
        self.user_repository = UserRepository.get_instance()

    def authenticate_user(self, username: str, password: str):
        user = self.user_repository.get_by_username(username)
        user.verify_password(password)
        return user

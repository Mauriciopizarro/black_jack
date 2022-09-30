from repositories.user_pyson_repository import UserPysonRepository


class LoginService:

    def __init__(self):
        self.user_repository = UserPysonRepository.get_instance()

    def authenticate_user(self, username: str, password: str):
        user = self.user_repository.get_by_username(username)
        user.verify_password(password)
        return user

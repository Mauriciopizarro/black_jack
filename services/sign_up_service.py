from passlib.context import CryptContext
from repositories.user_pyson_repository import UserPysonRepository


class SignUpService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self):
        self.user_repository = UserPysonRepository.get_instance()

    def sign_up(self, username, plain_password):

        if not plain_password:
            raise EmptyPasswordError()

        if self.user_repository.is_existent_user(username):
            raise UserExistent()

        database = self.user_repository.user_db
        hashed_password = self.pwd_context.hash(plain_password)
        database.add({"username": username, "hashed_password": hashed_password})


class EmptyPasswordError(Exception):
    pass


class UserExistent(Exception):
    pass

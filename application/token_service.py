from dependency_injector.wiring import Provide, inject
from domain.interfaces.auth_provider import AuthProvider
from domain.user import User, UserInDB
from infrastructure.injector import Injector
from datetime import datetime, timedelta
from jose import jwt
from domain.interfaces.user_repository import UserRepository

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 9999999


class TokenService:

    @staticmethod
    def generate_token(user: User):
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        expire = datetime.utcnow() + expires_delta
        to_encode = {
            "exp": expire,
            "sub": user.username
        }
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    @inject
    def get_user_by_token(token: str, user_repository: UserRepository = Provide[Injector.user_repo], auth_provider: AuthProvider = Provide[Injector.auth_provider]) -> UserInDB:
        user_data = auth_provider.get_user_data(token)
        user = user_repository.get_by_username(username=user_data["username"])
        return user


class InvalidTokenError(Exception):
    pass

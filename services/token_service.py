
from models.user import User
from datetime import datetime, timedelta
from jose import jwt, JWTError

from repositories.user_pyson_repository import UserPysonRepository

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


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
    def get_user_by_token(token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise InvalidTokenError()
        except JWTError:
            raise InvalidTokenError()
        repository = UserPysonRepository.get_instance()
        user = repository.get_by_username(username=username)
        return user


class InvalidTokenError(Exception):
    pass

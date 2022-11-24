from typing import Dict
from jose import jwt, JWTError
from api_gateway.domain.interfaces.auth_provider import AuthProvider

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 9999999


class LocalAuthProvider(AuthProvider):

    def get_user_data(self, token: str) -> Dict:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise InvalidTokenError()
        except JWTError:
            raise InvalidTokenError()
        return {"username": username}


class InvalidTokenError(Exception):
    pass

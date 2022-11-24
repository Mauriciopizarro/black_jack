from typing import Optional
from pydantic import BaseModel, validator
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    username: str
    id: Optional[str]


class UserInDB(User):
    hashed_password: str

    def verify_password(self, plain_password):
        if not pwd_context.verify(plain_password, self.hashed_password):
            raise IncorrectPasswordError


class UserPlainPassword(User):
    plain_password: str

    def get_hashed_password(self):
        return pwd_context.hash(self.plain_password)

    @validator("plain_password")
    def validate_plain_password(cls, value):
        if not value:
            raise EmptyPasswordError()
        return value


class IncorrectPasswordError(Exception):
    pass


class EmptyPasswordError(Exception):
    pass

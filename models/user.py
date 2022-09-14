from uuid import UUID
from pydantic import BaseModel
from typing import Union
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    user_id: UUID
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str

    def verify_password(self, plain_password):
        if not pwd_context.verify(plain_password, self.hashed_password):
            raise IncorrectPasswordError


class IncorrectPasswordError(Exception):
    pass

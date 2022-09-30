from pydantic import BaseModel
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    username: str
    id: int


class UserInDB(User):
    hashed_password: str

    def verify_password(self, plain_password):
        if not pwd_context.verify(plain_password, self.hashed_password):
            raise IncorrectPasswordError


class IncorrectPasswordError(Exception):
    pass


class NotExistentUser(Exception):
    pass

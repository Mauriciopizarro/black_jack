from abc import ABC, abstractmethod
from models.user import UserInDB, UserPlainPassword


class UserRepository(ABC):

    @abstractmethod
    def get_by_username(self, username: str) -> UserInDB:
        pass

    @abstractmethod
    def save_user(self, user: UserPlainPassword) -> UserPlainPassword:
        pass


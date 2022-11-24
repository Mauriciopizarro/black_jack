from pysondb import db
from game_service.application.exceptions import NotExistentUser, UserExistent
from api_gateway.domain.user import UserInDB, UserPlainPassword
from api_gateway.domain.interfaces.user_repository import UserRepository


class UserPysonRepository(UserRepository):
    instance = None

    def __init__(self):
        self.user_db = db.getDb("black_jack_users.json")

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
            cls.user_db = db.getDb("black_jack_users.json")

        return cls.instance

    def get_by_username(self, username):
        query_result = self.user_db.getBy({"username": username})
        if not query_result:
            raise NotExistentUser()
        user_dict = query_result[0]
        return UserInDB(**user_dict)

    def save_user(self, user: UserPlainPassword):
        query_result = self.user_db.getBy({"username": user.username})
        if len(query_result) > 0:
            raise UserExistent()
        hashed_password = user.get_hashed_password()
        user_id = self.user_db.add({"username": user.username, "hashed_password": hashed_password})
        return UserInDB(hashed_password=hashed_password, id=user_id, username=user.username)

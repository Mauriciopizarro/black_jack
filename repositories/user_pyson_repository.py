from pysondb import db
from models.user import UserInDB, NotExistentUser


class UserPysonRepository:
    instance = None

    # Patron singleton
    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
            cls.user_db = db.getDb("black_jack_users.json")

        return cls.instance

    def get_by_username(self, username):
        query_result = self.user_db.getBy({"username": username})
        if len(query_result) == 0:
            raise NotExistentUser()
        user_dict = query_result[0]
        return UserInDB(**user_dict)

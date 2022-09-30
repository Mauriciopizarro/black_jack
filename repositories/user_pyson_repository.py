from pysondb import db
from models.user import UserInDB, NotExistentUser

"""fake_users_db = {
    "Mauri": {
        "username": "Mauri",
        "full_name": "Mauricio Pizarro",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "user_id": uuid.uuid4(),
        "disabled": False,
    },
    "More": {
        "username": "More",
        "full_name": "Morena Cortez",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "user_id": uuid.uuid4(),
        "disabled": False,
    }
}
"""


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

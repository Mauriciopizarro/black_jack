import uuid

from models.user import UserInDB

fake_users_db = {
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


class UserRepository:
    instance = None

    # Patron singleton
    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()

        return cls.instance

    def get_by_username(self, username):
        if username not in fake_users_db:
            raise NotExistentUser()

        user_dict = fake_users_db[username]
        return UserInDB(**user_dict)


class NotExistentUser(Exception):
    pass

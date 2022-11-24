from sqlalchemy.orm import Session
from game_service.application.exceptions import UserExistent, NotExistentUser
from api_gateway.domain.interfaces.user_repository import UserRepository
from api_gateway.domain.user import UserPlainPassword, UserInDB
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, select
from sqlalchemy.sql.sqltypes import Integer, String

Base = declarative_base()


class UserSqlRepository(UserRepository):
    instance = None

    def __init__(self):
        self.engine = self.get_database()

    # Patron singleton
    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()

        return cls.instance

    @staticmethod
    def get_database():
        engine = db.create_engine('mysql+pymysql://user:password@mysql/blackjack')
        Base.metadata.create_all(engine)
        return engine

    def get_by_username(self, username):
        session = Session(self.engine)
        query = select(DbUser).where(DbUser.name == username)
        user_db = session.scalars(query).first()
        if user_db is None:
            raise NotExistentUser()
        return UserInDB(hashed_password=user_db.password, id=user_db.id, username=user_db.name)

    def save_user(self, user: UserPlainPassword):
        session = Session(self.engine)
        query = select(DbUser).where(DbUser.name == user.username)
        user_db = session.scalars(query).first()
        if user_db:
            raise UserExistent()
        hashed_password = user.get_hashed_password()
        userdb = DbUser(name=user.username, password=hashed_password)
        session.add(userdb)
        session.commit()
        session.refresh(userdb)
        return UserInDB(hashed_password=hashed_password, id=str(userdb.id), username=user.username)


class DbUser(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(255))
    password = Column("password", String(255))

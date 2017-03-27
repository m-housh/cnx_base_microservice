from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from connexion_sql_utils import BaseMixin
from .config import DB_URI

engine = create_engine(DB_URI)
Session = scoped_session(
    sessionmaker(autocommit=False, expire_on_commit=False, bind=engine)
)


class MyBase(BaseMixin):

    @staticmethod
    def session_maker():
        return Session()


DbModel = declarative_base(cls=MyBase)

from sqlalchemy import Column, String

from ..db import DbModel


class Foo(DbModel):

    bar = Column(String(40), unique=True, nullable=False)

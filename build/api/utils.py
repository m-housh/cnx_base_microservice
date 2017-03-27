from .db import DbModel, engine
from .orm import *


def create_all():
    DbModel.metadata.create_all(bind=engine)

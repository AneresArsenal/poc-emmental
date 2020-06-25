from sqlalchemy import BigInteger, Column, String

from utils.db import Model


class User(Model):

    id = Column(BigInteger,
               primary_key=True,
               autoincrement=True)

    email = Column(String(20), nullable=False, unique=True)

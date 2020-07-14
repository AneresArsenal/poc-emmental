from sqlalchemy import Column, String, Text
from sqlalchemy_api_handler import ApiHandler

from utils.db import Model


class Tag(ApiHandler,
          Model):

    info = Column(Text())

    label = Column(String(128), unique=True)

from sqlalchemy import Column, String
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model


class User(ApiHandler,
           Model,
           HasScienceFeedbackMixin):

    email = Column(String(120), nullable=False, unique=True)

    firstName = Column(String(30))

    lastName = Column(String(30))

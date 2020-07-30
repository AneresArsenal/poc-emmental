import enum
from sqlalchemy import Column, \
                       Enum, \
                       String
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model


class ContentType(enum.Enum):
    article = 'article'
    post = 'post'
    video = 'video'


class Content(ApiHandler,
              Model,
              HasScienceFeedbackMixin):

    mediumId = Column(
        BigInteger(),
        ForeignKey('medium.id'),
        index=True
    )

    medium = relationship(
        'Medium',
        foreign_keys=[mediumId],
        backref='contents'
    )

    title = Column(String(40))

    type = Enum(ContentType)

    url = Column(String(300), nullable=False, unique=True)

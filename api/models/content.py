import enum
from sqlalchemy import Column, \
                       Enum, \
                       String, \
                       BigInteger, \
                       ForeignKey
from sqlalchemy.orm import relationship
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

    mediumId = Column(BigInteger(),
                      ForeignKey('medium.id'),
                        index=True)

    medium = relationship('Medium',
                            foreign_keys=[mediumId])

    title = Column(String(140))

    type = Enum(ContentType)

    url = Column(String(512), nullable=False, unique=True)

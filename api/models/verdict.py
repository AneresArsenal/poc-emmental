from sqlalchemy import BigInteger, \
                       Column, \
                       Enum, \
                       ForeignKey, \
                       String
from sqlalchemy.orm import relationship
from sqlalchemy_api_handler import ApiHandler

from models.mixins.has_science_feedback_mixin import HasScienceFeedbackMixin
from utils.db import Model


class Verdict(ApiHandler,
              Model,
              HasScienceFeedbackMixin):

    claimId = Column(BigInteger(),
                     ForeignKey('claim.id'),
                     index=True)

    claim = relationship('Claim',
                         backref='verdicts',
                         foreign_keys=[claimId])

    contentId = Column(BigInteger(),
                       ForeignKey('content.id'),
                       index=True)

    content = relationship('Content',
                           foreign_keys=[contentId],
                           backref='verdicts')

    editorId = Column(BigInteger(),
                      ForeignKey('user.id'),
                      nullable=False,
                      index=True)

    editor = relationship('User',
                          foreign_keys=[editorId],
                          backref='verdicts')

    title = Column(String(30))

# pylint: disable=C0415
# pylint: disable=W0611

from utils.db import db
from repository.keywords import import_keywords


def import_models(with_creation=False):
    # *TBW*
    from models.appearance import Appearance
    from models.author_content import AuthorContent
    from models.claim import Claim
    from models.content import Content
    from models.medium import Medium
    from models.organization import Organization
    from models.review import Review
    from models.tag import Tag
    from models.user import User
    from models.verdict_reviewer import VerdictReviewer
    from models.verdict_tag import VerdictTag
    from models.verdict import Verdict

    if with_creation:
        db.create_all()
        db.session.commit()

    import_keywords()

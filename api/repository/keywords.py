from sqlalchemy import func, Index, TEXT
from sqlalchemy.sql.expression import cast
from sqlalchemy.sql.functions import coalesce

from models.content import Content
from models.review import Review
from models.tag import Tag
from models.user import User
from models.verdict import Verdict


def create_tsvector(*args):
    exp = args[0]
    for e in args[1:]:
        exp += ' ' + e
    return func.to_tsvector('english', exp)


def import_keywords():
    User.__ts_vector__ = create_tsvector(
        cast(coalesce(User.email, ''), TEXT),
        cast(coalesce(User.firstName, ''), TEXT),
        cast(coalesce(User.lastName, ''), TEXT),
    )
    User.__table_args__ = (
        Index(
            'idx_user_fts',
            User.__ts_vector__,
            postgresql_using='gin'
        ),
    )

    Verdict.__ts_vector__ = create_tsvector(
        cast(coalesce(Verdict.title, ''), TEXT),
    )
    Verdict.__table_args__ = (
        Index(
            'idx_verdict_fts',
            Verdict.__ts_vector__,
            postgresql_using='gin'
        ),
    )
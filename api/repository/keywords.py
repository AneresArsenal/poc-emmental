from sqlalchemy import func, Index, TEXT
from sqlalchemy.sql.expression import cast
from sqlalchemy.sql.functions import coalesce

from models.verdict import Verdict
from models.user import User



def create_tsvector(*targets):
    exp = targets[0]
    # joining each word in a single text
    for target in targets[1:]:
        exp += ' ' + target
    
    # create tsvector using english
    return func.to_tsvector('english', exp)


def import_keywords():
    #         Claim.__ts_vector__ = create_tsvector(
    #     # cast into text
    #     # coalesce remove null values
    #     cast(coalesce(Claim.text, ''), TEXT),
    # )

    #     # create a customized schema using the ts vector as a GIN index
    # Claim.__table_args__ = (
    #     Index(
    #         'idx_claim_fts',
    #         Claim.__ts_vector__,
    #         postgresql_using='gin'
    #     ),
    # )


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
from sqlalchemy.sql.expression import and_, or_

from models.tag import Tag
from models.user import User
from models.verdict import Verdict
from models.verdict_tag import VerdictTag


def verdict_ts_filter(ts_query):
    return or_(
        *[
            model.__ts_vector__.match(
                ts_query,
                postgresql_regconfig='english'
            )
            for model in [User, Verdict]
        ]
    )


def keep_verdicts_with_keywords_chain(query, keywords_chain):
    query = query.join(User)

    ts_queries = ['{}:*'.format(keyword) for keyword in keywords_chain.split(' ')]
    ts_filters = [
        verdict_ts_filter(ts_query)
        for ts_query in ts_queries
    ]
    query = query.filter(and_(*ts_filters))
    return query


def keep_verdicts_with_tag(query, tag):
    return query.join(VerdictTag) \
                .join(Tag) \
                .filter(Tag.label == tag)

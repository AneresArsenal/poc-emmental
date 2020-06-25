from models.user import User
from utils.db import db


def clean():
    ''' Order of deletions matters because of foreign key constraints '''
    print('clean all the database...')
    User.query.delete()
    db.session.commit()
    print('clean all the database...Done.')

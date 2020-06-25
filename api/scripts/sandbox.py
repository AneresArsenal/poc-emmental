from flask import current_app as app


from models.user import User
from repository.clean import clean
from utils.db import db


@app.manager.command
def sandbox():
    clean()

    print('create one user...')
    user = User()
    user.id = 0
    user.email = "foo.bar@me.me"

    db.session.add(user)
    db.session.commit()
    print('create one user...Done.')

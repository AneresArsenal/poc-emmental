# pylint: disable=W0612
# pylint: disable=W0613

import os
from flask_cors import CORS
from flask_script import Manager
from sqlalchemy_api_handler import ApiHandler

from models import import_models
from routes import import_routes
from scripts import install_scripts
from utils.db import db


def setup(flask_app,
          with_cors=False,
          with_models_creation=False,
          with_scripts_manager=False,
          with_routes=False):

    flask_app.secret_key = os.environ.get('FLASK_SECRET', '+%+5Q83!abR+-Dp@')
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSTGRES_URL')
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = flask_app
    db.init_app(flask_app)
    ApiHandler.set_db(db)

    @flask_app.teardown_request
    def remove_db_session(exc):
        try:
            # *TBW*
            db.session.remove()
        except AttributeError:
            pass

    if with_cors:
        # *TBW*
        CORS(flask_app,
             resources={r"/*": {"origins": "*"}},
             supports_credentials=True)

    # *TBW*
    flask_app.url_map.strict_slashes = False

    flask_app.app_context().push()
    import_models(with_creation=with_models_creation)

    if with_routes:
        import_routes()

    if with_scripts_manager:
        def create_app(env=None):
            flask_app.env = env
            return flask_app
        flask_app.manager = Manager(create_app)
        install_scripts()

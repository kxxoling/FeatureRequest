from flask import Flask

from .oauth import oauth, oauth_client
from .api import api
from .views import static_view

from .models import db
from .login import register_login
from .admin import register_admin


def create_app(default_config=None, config_spec=None):
    app = Flask(
        __name__,
        static_folder='dist/static'
    )

    app.config.from_pyfile(default_config)
    if app.config.get('LOCAL_CONFIG'):
        app.config.from_pyfile(app.config['LOCAL_CONFIG'])
    if isinstance(config_spec, dict):
        app.config.update(config_spec)

    #: prepare for database
    db.init_app(app)
    app.db = db

    register_oauth(app, oauth_client)
    register_routes(app)
    register_admin(app, db)
    register_login(app)
    return app


def register_routes(app):
    app.register_blueprint(api)
    app.register_blueprint(oauth)
    app.register_blueprint(static_view)     # TODO: Only in production


def register_oauth(app, o):
    app.config['GITHUB'].update(dict(
        request_token_params={'scope': 'user:email'},
        base_url='https://api.github.com/',
        request_token_url=None,
        access_token_method='POST',
        access_token_url='https://github.com/login/oauth/access_token',
        authorize_url='https://github.com/login/oauth/authorize')
    )
    o.init_app(app)

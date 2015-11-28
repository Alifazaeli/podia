__author__ = 'ali'


# import Flask
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_admin import Admin
from flask.ext.basicauth import BasicAuth

import sys

app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager()
admin = Admin(app, name='Podia', template_mode='bootstrap3')
basic_auth = BasicAuth(app)


def create_app(config=None):
    configure_app(app, config)
    configure_blueprints(app)
    login_manager.init_app(app)
    db.init_app(app)

    from project.config import config_dashboard_pages
    config_dashboard_pages()

    return app


def configure_app(app, config):
    app.config.from_object(config)
    app.config.from_envvar('project_CONFIG', silent=True)
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)


def configure_blueprints(app):
    app.config.setdefault('INSTALLED_BLUEPRINTS', [])
    blueprints = app.config['INSTALLED_BLUEPRINTS']
    for blueprint_name in blueprints:
        bp = __import__('project.controller.{0}'.format(blueprint_name), fromlist=[blueprint_name])
        app.register_blueprint(bp.api)


# def handle_exception(exc_type, exc_value, exc_traceback):
#     print(str(exc_type) + ' --- ' + str(exc_value) + ' --- ' + str(exc_traceback))
#
# sys.excepthook = handle_exception


@login_manager.request_loader
def load_user(request):

    from project.models.user import User

    token = request.headers.get('Authorization', '')

    if token:
        user_entry = User.get_user(token=token)
        if user_entry:
            return user_entry
    return None
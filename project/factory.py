__author__ = 'ali'


# import Flask
from flask_login import LoginManager
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager()


def create_app(config=None):
    configure_app(app, config)
    configure_blueprints(app)
    login_manager.init_app(app)
    db.init_app(app)
    return app


def configure_app(app, config):
    app.config.from_object(config)
    app.config.from_envvar('project_CONFIG', silent=True)


def configure_blueprints(app):
    app.config.setdefault('INSTALLED_BLUEPRINTS', [])
    blueprints = app.config['INSTALLED_BLUEPRINTS']
    for blueprint_name in blueprints:
        bp = __import__('project.controller.{0}'.format(blueprint_name), fromlist=[blueprint_name])
        app.register_blueprint(bp.api)



def handle_exception(exc_type, exc_value, exc_traceback):
    print(str(exc_type) + ' --- ' + str(exc_value) + ' --- ' + str(exc_traceback))



sys.excepthook = handle_exception

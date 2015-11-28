__author__ = 'ali'

# coding: utf-8
import os
from project.factory import app, admin, db
from flask_admin.contrib.sqla import ModelView
from project.models.user import User
from project.models.channel import Channel


class DefaultConfig(object):
    DEBUG = True

    ACCEPT_LANGUAGES = ['fa', 'en']
    BABEL_DEFAULT_LOCALE = 'fa'
    BABEL_DEFAULT_TIMEZONE = 'Asia/tehran'

    INSTALLED_BLUEPRINTS = (
        'api', 'admin'
    )

    app.config['BASIC_AUTH_USERNAME'] = 'ali'
    app.config['BASIC_AUTH_PASSWORD'] = 'af1992'


class DevelopmentConfig(DefaultConfig):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@localhost:5432/podia'.format(
        os.environ.get('PG_USERNAME', 'ali'),
        os.environ.get('PG_PASSWORD', '123456')
    )

    MINIFY_PAGE = False

    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'


class DeploymentConfig(DefaultConfig):
    DEBUG = False


class UserView(ModelView):

    column_exclude_list = ['id', 'password', 'token']

    column_editable_list = ['email', 'password']
    page_size = 20

    column_editable_list = ('user_name', 'email')


def config_dashboard_pages():
    admin.add_view(UserView(User, db.session))
    admin.add_view(ModelView(Channel, db.session))



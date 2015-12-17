__author__ = 'ali'

# coding: utf-8
import os
from project.factory import app, admin, db
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from project.models.user import User
from project.models.channel import Channel
from project.models.podcast import Podcast
import uuid


path = os.path.join(os.path.dirname(__file__), 'static')


class DefaultConfig(object):
    DEBUG = True

    ACCEPT_LANGUAGES = ['fa', 'en']
    BABEL_DEFAULT_LOCALE = 'fa'
    BABEL_DEFAULT_TIMEZONE = 'Asia/tehran'

    INSTALLED_BLUEPRINTS = [
        'api'
    ]

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
    form_excluded_columns = ['uuid']
    page_size = 20

    def on_model_change(self, form, model, is_created):
        if len(model.name):
            model.uuid = str(uuid.uuid3(uuid.NAMESPACE_DNS, model.name))


class ChannelView(ModelView):
    column_hide_backrefs = True
    form_excluded_columns = ['uuid']

    # Generate new hash on `name` change
    def on_model_change(self, form, model, is_created):
        if len(model.name):
            model.uuid = str(uuid.uuid3(uuid.NAMESPACE_DNS, model.name))


class PodcastView(ModelView):
    column_hide_backrefs = True
    form_excluded_columns = ['uuid']

    def on_model_change(self, form, model, is_created):
        if len(model.name):
            model.uuid = str(uuid.uuid3(uuid.NAMESPACE_DNS, model.name))


class FileManager(FileAdmin):
    can_delete = False


def config_dashboard_pages():
    admin.add_view(UserView(User, db.session))
    admin.add_view(ChannelView(Channel, db.session))
    admin.add_view(PodcastView(Podcast, db.session))
    admin.add_view(FileManager(path, name='Static Files'))
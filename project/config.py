__author__ = 'ali'

# coding: utf-8
import os


class DefaultConfig(object):
    DEBUG = True

    ACCEPT_LANGUAGES = ['fa', 'en']
    BABEL_DEFAULT_LOCALE = 'fa'
    BABEL_DEFAULT_TIMEZONE = 'Asia/tehran'

    INSTALLED_BLUEPRINTS = (
        'api',
    )


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@localhost:5432/podcast'.format(
        os.environ.get('PG_USERNAME', 'ali'),
        os.environ.get('PG_PASSWORD', '123456')
    )

    MINIFY_PAGE = False


class DeploymentConfig(DefaultConfig):
    DEBUG = False


__author__ = 'ali'

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from project.config import DevelopmentConfig
from project.factory import db, create_app

app = create_app(DevelopmentConfig)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
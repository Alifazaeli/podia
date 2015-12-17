s__author__ = 'ali'

from project.factory import db
from project.utils.serializer import dump_datetime
import datetime


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Unicode, unique=True, nullable=False)
    uuid = db.Column(db.Unicode, unique=True)
    user_name = db.Column(db.Unicode, nullable=False)
    password = db.Column(db.Unicode)
    devices = db.Column(db.Unicode)
    podcast_played_counter = db.Column(db.Integer, default=0)
    # device_id = db.Column(db.Unicode)
    token = db.Column(db.Unicode)

    def __str__(self):
        return self.user_name + ' - ' + self.email

    def as_dict(self, ignorefields):
        """
        this method convert sqlalchemy object to dict

        :param: self : object of models
        :type : object
        :param : ignorefields
        :type : list of ignore fields
        :rtype : dict
        """
        result = {}
        for key in self.__mapper__.c.keys():
            if key not in ignorefields:
                if type(getattr(self, key)) == datetime:
                    result[key] = dump_datetime(getattr(self, key))
                else:
                    result[key] = getattr(self, key)
        return result

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get(**kwargs):
        return User.query.filter_by(**kwargs).first()
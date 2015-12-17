II__author__ = 'ali'

from project.factory import db
from project.utils.serializer import dump_datetime
from sqlalchemy import event

from collections import OrderedDict
from datetime import datetime
import uuid


class Channel(db.Model):
    __tablename__ = 'channel'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Unicode, unique=True, nullable=False)
    uuid = db.Column(db.Unicode, unique=True)
    description = db.Column(db.Unicode)
    creation_date = db.Column(db.DateTime, default=datetime.now)
    views = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('user_ref', lazy='dynamic'))



    def __str__(self):
        return self.name

    def as_dict(self, ignorefields):
        """
        this method convert sqlalchemy object to dict

        :param: self : object of models
        :type : object
        :param : ignorefields
        :type : list of ignore fields
        :rtype : dict
        """
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            if key not in ignorefields:
                if type(getattr(self, key)) == datetime:
                    result[key] = dump_datetime(getattr(self, key))
                else:
                    result[key] = getattr(self, key)
        return result

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get(**kwargs):
        return Channel.query.filter_by(**kwargs).first()
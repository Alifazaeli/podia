__author__ = 'ali'

from project.factory import db
from project.utils.serializer import dump_datetime
import datetime
from collections import OrderedDict


class Podcast(db.Model):
    __tablename__ = 'podcast'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Unicode)
    like = db.Column(db.Integer, default=0)
    run_time = db.Column(db.Integer, default=0)
    description = db.Column(db.Unicode)
    url = db.Column(db.Unicode)
    image = db.Column(db.Unicode)
    time = db.Column(db.Time)
    upload_time = db.Column(db.DateTime, default=datetime.datetime.now)

    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'), nullable=False)
    channel = db.relationship('Channel', backref=db.backref('channel_ref', lazy='select'), lazy='select')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User')

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
                if type(getattr(self, key)) == datetime.datetime:
                    result[key] = dump_datetime(getattr(self, key))
                else:
                    result[key] = getattr(self, key)

        result['channel'] = self.channel.as_dict(['id', 'views'])
        return result

    @staticmethod
    def get(limit, **kwargs):
        return Podcast.query.filter_by(**kwargs).limit(limit).all()

__author__ = 'ali'

from project.factory import db
import datetime


class Podcast(db.Model):
    __tablename__ = 'podcast'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Unicode)
    likes = db.Column(db.Unicode)
    links = db.Column(db.Unicode)
    play_counter = db.Column(db.Integer)
    note = db.Column(db.Unicode)
    url = db.Column(db.Unicode)
    image = db.Column(db.Unicode)
    upload_time = db.Column(db.DateTime, default=datetime.datetime.now)
    channel_rel = db.Column(db.Integer, db.ForeignKey('channel.id'))
    user_rel = db.Column(db.Integer, db.ForeignKey('user.id'))

    @staticmethod
    def get(**kwargs):
        return Podcast.query.filter_by(**kwargs)
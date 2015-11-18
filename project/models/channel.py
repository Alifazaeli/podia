__author__ = 'ali'


from project.factory import db
from datetime import datetime
from sqlalchemy import UniqueConstraint
import uuid


class Channel(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Unicode, nullable=False)
    uuid = db.Column(db.Text, unique=True, default=uuid.uuid3(uuid.NAMESPACE_DNS, name))
    description = db.Column(db.Unicode)
    creation_date = db.Column(db.DateTime, datetime.now)
    views = db.Column(db.Integer, default=0)
    followers = db.Column(db.Integer, default=0)
    owners = db.Column(db.ForeignKey('user.id'))

    __table_args__ = (UniqueConstraint('name', name='name__unique_channel_key'), )

    def add_channel(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_channel(**kwargs):
        return Channel.query.filter_by(**kwargs).first()
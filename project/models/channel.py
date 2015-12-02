II__author__ = 'ali'

from project.factory import db
from datetime import datetime
from sqlalchemy import UniqueConstraint
import uuid


class Channel(db.Model):
    __tablename__ = 'channel'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Unicode, unique=True, nullable=False)
    uuid = db.Column(db.Unicode, unique=True, default=str(uuid.uuid3(uuid.NAMESPACE_DNS, str(datetime.now()))))
    description = db.Column(db.Unicode)
    creation_date = db.Column(db.DateTime, default=datetime.now)
    views = db.Column(db.Integer, default=0)
    followers = db.Column(db.Integer, default=0)
    user_rel = db.Column(db.Integer, db.ForeignKey('user.id'))

    # __table_args__ = (UniqueConstraint('name', name='name__unique_channel_key'), )

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get(**kwargs):
        return Channel.query.filter_by(**kwargs).first()
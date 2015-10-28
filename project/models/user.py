__author__ = 'ali'

from project.factory import db
from sqlalchemy import UniqueConstraint
from sqlalchemy.exc import IntegrityError, InvalidRequestError


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Unicode, unique=True, nullable=False)
    user_name = db.Column(db.Unicode, nullable=False)
    password = db.Column(db.Unicode)
    devices = db.Column(db.Unicode)
    podcast_played_counter = db.Column(db.Integer)
    device_id = db.Column(db.Unicode)
    token = db.Column(db.Unicode)

    __table_args__ = (UniqueConstraint('email', name='email__unique_user_key'), )

    def add_user(self):

        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError as ex:
            return

    @staticmethod
    def get_user(email, password):
        return User.query.filter(email == email, password == password).first()
        # return User.query.filter(**kwargs)
__author__ = 'ali'

from project.factory import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.Unicode)
    email = db.Column(db.Unicode)
    password = db.Column(db.Unicode)
    devices = db.Column(db.Unicode)
    podcast_played_counter = db.Column(db.Integer)
    device_id = db.Column(db.Unicode)

    def add_user(self):
        db.session.add(self)
        db.session.commit()
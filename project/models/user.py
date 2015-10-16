__author__ = 'ali'

from project.factory import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.Unicode)
    email = db.Column(db.Unicode)
    password = db.Column(db.Unicode)
    devices = db.Column(db.Unicode)
    podcast_played_counter = db.column(db.Integer)
    device_id = db.column(db.Unicode)
__author__ = 'ali'

from project.factory import db
import datetime

class podcast(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincreament=True)
    name = db.Column(db.Unicode)
    likes = db.Column(db.Unicode)
    play_counter = db.Column(db.Integer)
    note = db.Column(db.Unicode)
    url = db.Column(db.Unicode)
    image = db.Column(db.Unicode)

    upload_time = db.Column(db.DATETIME, default=datetime.datetime.now)

    #publisher
    #user
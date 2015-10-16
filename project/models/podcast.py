__author__ = 'ali'

from project.factory import db
import datetime

class podcast(db.Model):

    id = db.column(db.Integer, primary_key=True, autoincreament=True)
    name = db.column(db.Unicode)
    likes = db.column(db.Unicode)
    play_counter = db.Column(db.Integer)
    note = db.column(db.Unicode)
    url = db.column(db.Unicode)
    image = db.column(db.Unicode)

    upload_time = db.column(db.DATETIME, default=datetime.datetime.now)

    #publisher
    #user
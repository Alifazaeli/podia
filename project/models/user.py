__author__ = 'ali'

from sqlalchemy import *
from project.factory import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.Unicode)
    password = db.Column(db.Unicode)
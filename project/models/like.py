__author__ = 'ali'

from project.factory import db


class PodcastLike(db.Model):
    __tablename__ = 'podcastlike'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    podcast_id = db.Column(db.Integer, db.ForeignKey('podcast.id'), nullable=True)
    podcast = db.relation('Podcast', backref=db.backref('podcast_ref', lazy='dynamic'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = db.relation('User')
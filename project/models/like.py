__author__ = 'ali'

from project.factory import db


class PodcastLike(db.Model):
    __tablename__ = 'podcastlike'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    podcast_id = db.Column(db.Integer, db.ForeignKey('podcast.id'), nullable=False)
    podcast = db.relation('Podcast', backref=db.backref('podcast_ref', lazy='dynamic'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relation('User')


    __table_args__ = (db.UniqueConstraint('podcast_id', 'user_id', name='_podcast_user_unique_key'),)

    def add(self):
        db.session.add(self)
        db.session.commit()
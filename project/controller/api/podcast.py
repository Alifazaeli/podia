__author__ = 'ali'


from project.models.podcast import Podcast
from project.models.channel import Channel
from project.models.like import PodcastLike
from flask.ext.login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify
from . import api
import json


@api.route('/podcast/timeline', methods=['GET'])
def timeline():
    """
    :rtype : json
    """
    podcasts = Podcast().get(limit=10)
    total = []
    for item in podcasts:
        total.append(item.as_dict(['user_id', 'channel_id']))

    return json.dumps({'podcasts': total}), 200


@api.route('/podcast', methods=['GET', 'POST'])
def podcast():
    uuid = request.form.get('uuid', None)
    channel_uuid = request.form.get('channel_uuid', None)

    if uuid:
        podcasts = Podcast().get(limit=10, uuid=uuid)
    elif channel_uuid:
        channel = Channel.get(uuid=channel_uuid)
        podcasts = Podcast.get(limit=10, channel=channel)

    total = []
    for item in podcasts:
        total.append(item.as_dict(['id', 'user_id', 'channel_id']))

    return json.dumps({'podcasts': total}), 200


@api.route('/podcast/like', methods=['GET', 'POST'])
@login_required
def podcast_like():

    liked_podcast = PodcastLike()
    podcast_uuid = request.form.get('podcast_uuid', None)
    liked_podcast.podcast = Podcast.get(1, uuid=podcast_uuid)[0]
    liked_podcast.user = current_user
    try:
        liked_podcast.add()
        return jsonify(podcast=podcast_uuid, user=current_user.uuid), 201
    except IntegrityError:
        return jsonify(data='duplicate_error'), 409

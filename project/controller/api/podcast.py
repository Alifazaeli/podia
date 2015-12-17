__author__ = 'ali'

from flask import request
import json

from project.models.podcast import Podcast
from project.models.channel import Channel
from . import api


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
        total.append(item.as_dict(['user_id', 'channel_id']))

    return json.dumps({'podcasts': total}), 200
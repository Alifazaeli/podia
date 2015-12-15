__author__ = 'ali'

from flask import request
import json

from project.models.podcast import Podcast
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

    return json.dumps(total), 200


@api.route('/podcast', methods=['GET', 'POST'])
def podcast():
    uuid = request.form.get('uuid', None).encode('utf-8')
    channel_Id = request.form.get('channel_id', None)

    podcasts = Podcast().get(limit=100, uuid=uuid, channel_id=channel_Id)
    total = []
    for item in podcasts:
        total.append(item.as_dict(['user_id', 'channel_id']))

    return json.dumps({'podcasts': total}), 200
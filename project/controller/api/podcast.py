__author__ = 'ali'

from flask import jsonify
import json

from project.models.podcast import Podcast
from . import api


@api.route('/podcast/timeline', methods=['GET'])
def podcast():

    podcasts = Podcast().get(limit=10)
    total = []
    for item in podcasts:
        total.append(item.as_dict(['user_id', 'channel_id']))

    return json.dumps(total), 200

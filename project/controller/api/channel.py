__author__ = 'ali'

# from project
from . import api
from project.models.channel import Channel


# from flask
import json
from flask import jsonify
from flask.ext.login import login_required


@login_required
@api.route('/get_channel/<channel_id>', methods=['GET'])
def get_channel(channel_id):
    return jsonify(data=Channel.get(id=channel_id)), 200
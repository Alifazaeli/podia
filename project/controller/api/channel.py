__author__ = 'ali'

# from project
from project.factory import app
from project.models.channel import Channel


# from flask
from flask import jsonify
from flask.ext.login import login_required


@app.route('/get_channel/<channel_id>', methods=['GET'])
@login_required
def get_channel(channel_id):
    return jsonify(Channel.get(id=channel_id)), 200
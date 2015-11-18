__author__ = 'ali'

# from project
from project.factory import app
from project.models.channel import Channel


# from flask
from Flask import jsonify

@app.route('/get_channel/<channel_id>', methods=['GET'])
def get_channel(channel_id):
    return jsonify(Channel.get_channel(id=channel_id))
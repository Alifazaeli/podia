__author__ = 'ali'

# from python and Flask
from flask import request, jsonify

# from project
from . import api
from project.models.user import User

@api.route('/add_user', methods=['get', 'POST'])
def add_user():

    user = User()
    user.user_name = request.form.get('user_name', '')
    user.device_id = request.form.get('device_id', '')
    user.devices = request.form.get('devices', '')
    user.email = request.form.get('email', '')
    user.password = request.form.get('password', '')
    user.image = request.form.get('image', '')
    user.add_user()

    return '200'



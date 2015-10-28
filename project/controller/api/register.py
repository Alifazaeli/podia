__author__ = 'ali'

# from python and Flask
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError

# from project
from . import api
from project.models.user import User


@api.route('/add_user', methods=['GET', 'POST'])
def add_user():

    try:
        user = User()
        user.user_name = request.form.get('user_name', None)
        user.device_id = request.form.get('device_id', '')
        user.devices = request.form.get('devices', '')
        user.email = request.form.get('email', None)
        user.password = request.form.get('password', None)
        user.image = request.form.get('image', '')
        user.token = hash(user.email)
        user.add_user()

        return jsonify(status=200, token=user.token)
    except IntegrityError:
        return jsonify(sataus=500, data='Duplicate_email')
    except Exception as ex:
        return jsonify(status=500, data=str(ex.args))


@api.route('/login', methods=['POST', 'GET'])
def login():

    email = request.form.get('email', '')
    password = request.form.get('password', '')

    user_obj = User.get_user(email, password)
    try:
        if user_obj:
            return jsonify(status=200, data=dict(user_name=user_obj.user_name, token=user_obj.token))
        else:
            return jsonify(status=404, data='Not Found!')
    except Exception as ex:
        return jsonify(status=500, data=ex.args)
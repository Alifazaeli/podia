__author__ = 'ali'

# from python and Flask
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from flask.ext.login import login_required

# from project
from . import api
from project.models.user import User

@api.route('/add_user', methods=['GET', 'POST'])
def add_user():

    try:
        user = User()
        user.user_name = request.form.get('user_name', None)
        user.device_id = request.form.get('device_id', '')
        user.devices = request.form.get('device_name', None)
        user.email = request.form.get('email', None)
        user.password = request.form.get('password', None)
        user.image = request.form.get('image', '')
        user.token = hash(user.email + user.password)
        user.add_user()

        return jsonify(status=201, token=user.token)
    except IntegrityError as ex:
        if ex.orig.pgcode == '23505':  # duplicate user
            return jsonify(status=409, data=ex.args)
        elif ex.orig.pgcode == '23502':  # required fields
            return jsonify(status=400, data=ex.args)
        else:
            return jsonify(status=400, data=ex.args)

    except Exception as ex:
        return jsonify(status=500, data=ex.args)


@api.route('/login', methods=['POST', 'GET'])
def login():

    try:
        email = request.form.get('email', '')
        password = request.form.get('password', '')

        if email and password:
            user_obj = User.get_user(email=email, password=password)
            if user_obj:
                return jsonify(status=200, data=dict(user_name=user_obj.user_name, token=user_obj.token))
            else:
                return jsonify(status=404, data='Not Found!')
        else:
            return jsonify(status=400, data='User_name or Password are required')
    except Exception as ex:
        return jsonify(status=500, data=ex.args)

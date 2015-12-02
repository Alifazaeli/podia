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
        user.devices = request.form.get('device_name', None)
        user.email = request.form.get('email', None)
        user.password = request.form.get('password', None)
        user.image = request.form.get('image', '')
        user.token = hash(user.email + user.password)
        user.add_user()

        return jsonify(token=user.token), 201
    except IntegrityError as ex:
        if ex.orig.pgcode == '23505':  # duplicate user
            return jsonify(data=ex.args), 409
        elif ex.orig.pgcode == '23502':  # required fields
            return jsonify(data=ex.args), 400
        else:
            return jsonify(data=ex.args), 400

    except Exception as ex:
        return jsonify(data=ex.args), 500


@api.route('/login', methods=['POST', 'GET'])
def login():
    try:
        email = request.form.get('email', '')
        password = request.form.get('password', '')

        if email and password:
            user_obj = User.get_user(email=email, password=password)
            if user_obj:
                return jsonify(data=dict(user_name=user_obj.user_name,
                                         token=user_obj.token,
                                         email=user_obj.email,
                                         )), 200
            else:
                return jsonify(data='Not Found!'), 404
        else:
            return jsonify(data='email or Password are required'), 400
    except Exception as ex:
        return jsonify(data=ex.args), 500
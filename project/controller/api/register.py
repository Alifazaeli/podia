__author__ = 'ali'

# from python and Flask
from flask import request, jsonify

# from project
from . import api



@api.route('/add_user', methods=['GET', 'POST'])
def add_user():

    dict = request.get_data()
    return jsonify(dict.get('test', ''))

    return '200'
# -*- coding: utf-8 -*-
import time
from flask import request, jsonify
from handlers import user
from test_res import task16
from utils.util import test_api


@user.route('/user_info', methods=['POST', 'GET'])
def user_info():
    test_api(request)
    return jsonify(task16)


@user.route('/save_user_info', methods=['POST', 'GET'])
def save_user_info():
    test_api(request)
    return jsonify(task16)
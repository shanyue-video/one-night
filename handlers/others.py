# -*- coding: utf-8 -*-
from flask import request, jsonify
from handlers import other
from test_res import task22, task1
from utils.models import Upload


@other.route('/feed_back', methods=['POST', 'GET'])
def feed_back():
    userid = request.args.get('userid', '')
    content = request.args.get('content', '')
    return jsonify(task22)


@other.route('/get_carousel', methods=['POST', 'GET'])
def get_carousel():
    class_objs = Upload.objects
    for o in class_objs:
        print o
    return jsonify(task1)
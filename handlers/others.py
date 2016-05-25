# -*- coding: utf-8 -*-
from flask import request, jsonify
from handlers import other
from test_res import task22


@other.route('/Feedback', methods=['POST', 'GET'])
def feed_back():
    userid = request.args.get('userid', '')
    content = request.args.get('content', '')
    return jsonify(task22)
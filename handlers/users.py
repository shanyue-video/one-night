# -*- coding: utf-8 -*-
import json
from flask import request, jsonify
from handlers import user
from test_res import task16


@user.route('/user_info', methods=['POST', 'GET'])
def user_info():
    userid = eval(request.args.get('args'))#.           #to_dict().get('userid')
    print('xxx', userid)
    return jsonify(task16)

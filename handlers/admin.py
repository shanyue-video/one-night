# -*- coding: utf-8 -*-
from flask import request, jsonify
from handlers import user
from test_res import task16


@user.route('/Userinfo', methods=['POST', 'GET'])
def user_info():
    userid = request.args.get('userid', '')
    return jsonify(task16)


# app.register_blueprint(admin)
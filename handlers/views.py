# -*- coding: utf-8 -*-
from flask import jsonify, request, render_template
from handlers import view
from utils.models import UserForm
from utils.util import acquire_admin


@view.route('/login', methods=['POST', 'GET'])
def login():
    form = UserForm()
    return render_template('login.html', form=form)


@view.route('/upload')
@acquire_admin
def upload():
    userid = request.args.get('userid', '')
    print('xxx', userid)
    return jsonify({"aa": "bb"})

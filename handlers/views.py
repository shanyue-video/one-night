# -*- coding: utf-8 -*-
import hashlib
from flask import jsonify, request, render_template, session
import flask
from handlers import view
from mongoengine import DoesNotExist
from utils.models import UserForm, User
from utils.util import acquire_admin


@view.route('/login', methods=['POST', 'GET'])
def login():
    form = UserForm()
    return render_template('login.html', form=form)


@view.route('/login/validate', methods=['POST'])
def login_validate():
    m = hashlib.md5()
    user = User()
    form = UserForm(request.form, obj=user)
    form.populate_obj(user)
    m.update(user.password_hash)
    c_password = m.hexdigest()
    try:
        c_user = User.objects.get(username=user.username)
    except DoesNotExist:
        flask.abort(403)
    if c_user.password_hash == c_password:
        session['user'] = c_user.username
        session['role'] = c_user.role
    return flask.redirect(flask.url_for('view.upload'))


@view.route('/upload')
@acquire_admin
def upload():
    try:
        user = User.objects.get(username=session['user'])
    except DoesNotExist:
        flask.abort(403)
    print('xxx', user)
    # session.pop('role')
    return jsonify({"aa": "bb"})

# -*- coding: utf-8 -*-
import hashlib
import os
import time
from conf import UPLOAD_FOLDER
from flask import request, render_template, session
import flask
from handlers import view
from mongoengine import DoesNotExist, NotUniqueError
from utils.models import UserForm, User, UploadForm, Upload
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
    # print form.validate_on_submit()
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
    form = UploadForm(request.form)
    return render_template('upload.html', form=form)


@view.route('/upload/success')
@acquire_admin
def upload_success():
    return render_template('upload_success.html')


@view.route('/upload/validate', methods=['POST'])
def upload_validate():
    _file = request.files
    upload_obj = Upload()

    try:
        user = User.objects.get(username=session['user'])
    except DoesNotExist:
        flask.abort(403)
    form = UploadForm(request.form, obj=upload_obj)
    form.populate_obj(upload_obj)

    upload_obj.video = _file['video'].filename + '-' + str(time.time())
    upload_obj.picture = _file['img'].filename + '-' + str(time.time())

    upload_obj.user = user

    try:
        upload_obj.save()
    except NotUniqueError as e:
        print e.message
        return flask.abort(501)

    _file['video'].save(os.path.join(UPLOAD_FOLDER, upload_obj.class_name))
    _file['img'].save(os.path.join(UPLOAD_FOLDER, upload_obj.class_name))

    if not form.validate_on_submit():
        return flask.abort(403)
    return flask.redirect(flask.url_for('view.upload.success'))

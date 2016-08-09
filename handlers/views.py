# -*- coding: utf-8 -*-
import hashlib
import json
import time
import uuid
from pymongo.errors import AutoReconnect

from utils.celery_task import task
import os
from s3.get_url import get_url_qiniu
from utils.conf import UPLOAD_FOLDER
from flask import request, render_template, session
import flask
from flask import jsonify
from handlers import view
from mongoengine import DoesNotExist, NotUniqueError
from utils.extmodels.ext_models import Course, AppInfo
from utils.models import UserForm, User, UploadForm, Upload
from utils.util import acquire_admin, handle_request_post_arguments


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

    upload_obj.video = _file['video'].filename + '_' + str(uuid.uuid1())
    upload_obj.picture = _file['img'].filename + '_' + str(uuid.uuid1())

    upload_obj.user = user
    upload_obj.class_summary = request.form['summary'].encode('utf-8')

    _file['video'].save(os.path.join(UPLOAD_FOLDER, upload_obj.video.split('_')[-1]) + '_tmp')
    _file['img'].save(os.path.join(UPLOAD_FOLDER, upload_obj.img.split('_')[-1]) + '_tmp')

    try:
        upload_obj.save()
    except NotUniqueError as e:
        print e.message
        return flask.abort(501)

    Course(base_info=upload_obj, class_uuid=str(uuid.uuid1())).save()

    if not form.validate_on_submit():
        return flask.abort(403)
    return flask.redirect(flask.url_for('view.upload_success'))


@view.route('/editor')
def editor():
    return render_template('editor.html')


@view.route('/react_ajax', methods=['POST'])
def react_ajax():
    r = request
    d = r.form['data']
    AppInfo(content=d).save()
    return jsonify({'success': 1})


@view.route('/after_editor')
def after_editor():
    try:
        data = AppInfo.objects.order_by('-c_time')[0]
    except AutoReconnect:
        return flask.redirect(flask.url_for('view.after_editor'))
    s = json.dumps(data.content)
    d = json.loads(s)
    content = {
        'data': d,
    }
    return render_template('after_editor.html', **content)


@view.route('/my_cnd', methods=['POST', 'GET'])
def my_cdn():
    args_list = ['url']
    ags = handle_request_post_arguments(request, args_list)
    url = ags['url']
    _uuid = str(uuid.uuid1())
    new_url = _uuid + url.split('/')[-1]
    task.delay(url, _uuid)
    after_url = get_url_qiniu(new_url)
    return jsonify({'over': after_url})
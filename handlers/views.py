# -*- coding: utf-8 -*-
import hashlib
import json
import uuid
from pymongo.errors import AutoReconnect

from utils.celery_task import task
import os
from s3.get_url import get_url_qiniu
from utils.conf import UPLOAD_FOLDER
from flask import request, render_template, session
import flask
from flask import jsonify, redirect, url_for
from handlers import view
from mongoengine import DoesNotExist, NotUniqueError
from utils.extmodels.ext_models import Course, AppInfo
from utils.models import UserForm, User, UploadForm, Upload
from utils.util import acquire_admin, handle_request_post_arguments, u_path

from hurry.filesize import size as hurry_size


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


@view.route('/upload/list')
@acquire_admin
def upload_list():
    base_data = Upload.objects().order_by('-c_time')
    data = []
    for d in base_data:
        try:
            d.picture_size = hurry_size(int(d.picture_size))
        except ValueError:
            pass
        try:
            d.video_size = hurry_size(int(d.video_size))
        except ValueError:
            pass
        data.append(d)

    content = {
        'data': data,
    }
    return render_template('upload_list.html', **content)


@view.route('/upload/update')
@acquire_admin
def upload_update():
    t_id = request.args.get('id')
    t_op = request.args.get('op')
    data = Upload.objects.get(id=t_id)
    if t_op == 'del':
        c = Course.objects.get(base_info=data)
        c.delete()
        data.delete()
        return redirect(url_for('view.upload_list'))
    form = UploadForm(request.form, obj=data)
    content = {
        'form': form,
        'op_id': t_id
    }
    return render_template('upload.html', **content)


@view.route('/upload/validate', methods=['POST'])
def upload_validate():
    _file = request.files

    op_id = request.args.get('op_id')

    if len(op_id) > 8:
        upload_obj = Upload.objects.get(id=op_id)
    else:
        upload_obj = Upload()

    try:
        user = User.objects.get(username=session['user'])
    except DoesNotExist:
        flask.abort(403)
    form = UploadForm(request.form, obj=upload_obj)
    form.populate_obj(upload_obj)

    upload_obj.user = user
    upload_obj.class_summary = request.form['summary'].encode('utf-8')

    if len(_file['video'].filename) > 0:
        upload_obj.video = str(uuid.uuid1())
        filename = u_path(os.path.join(UPLOAD_FOLDER, upload_obj.video) + '_tmp0')
        _file['video'].save(filename)
        upload_obj.video_size = str(os.path.getsize(filename))
    if len(_file['img'].filename) > 0:
        upload_obj.picture = str(uuid.uuid1())
        filename = u_path(os.path.join(UPLOAD_FOLDER, upload_obj.picture) + '_tmp0')
        _file['img'].save(filename)
        upload_obj.picture_size = str(os.path.getsize(filename))

    try:
        upload_obj.save()
    except NotUniqueError as e:
        print e.message
        return flask.abort(501)

    if len(op_id) > 8:
        pass
    else:
        Course(base_info=upload_obj, class_uuid=str(uuid.uuid1())).save()

    if not form.validate_on_submit():
        return flask.abort(403)
    if len(_file['video'].filename) > 0:
        os.rename(u_path(os.path.join(UPLOAD_FOLDER, upload_obj.video) + '_tmp0'),
                  u_path(os.path.join(UPLOAD_FOLDER, upload_obj.video) + '_tmp'))
    if len(_file['img'].filename) > 0:
        os.rename(u_path(os.path.join(UPLOAD_FOLDER, upload_obj.picture) + '_tmp0'),
                  u_path(os.path.join(UPLOAD_FOLDER, upload_obj.picture) + '_tmp'))
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
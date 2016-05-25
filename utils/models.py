# -*- coding: utf-8 -*-
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongoengine.wtf import model_form

engine = MongoEngine()


class Test(engine.Document):
    email = engine.StringField(required=True)
    first_name = engine.StringField(max_length=50)
    last_name = engine.StringField(max_length=50)


class User(engine.Document):
    username = engine.StringField(required=True, max_length=20, unique=True,
                                  verbose_name=u'用户名', help_text=u'员工邮箱前缀')
    password_hash = engine.StringField(max_length=255, required=True,
                                       verbose_name=u'密码', help_text=u'用户密码')
    role = engine.StringField(required=True, default='user',
                              choices=(('user', u'普通用户'), ('admin', u'管理员')),
                              verbose_name=u'角色')

    def __unicode__(self):
        return self.username


UserForm = model_form(User, exclude=('role',))
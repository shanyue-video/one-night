# coding=utf-8
import os
# from utils.conf import INNER_IP, port

__author__ = 'dengjing'
bind = '0.0.0.0:8888'  # 绑定的端口
# bind = '%s:%s' % (INNER_IP, port)
workers = 4  # worker数量
backlog = 2048
# debug = True
proc_name = 'gunicorn.pid'
path = os.path.abspath(os.path.join(__file__, os.path.pardir))
pidfile = '%s/logs/gunicorn.log' % path
# loglevel = 'debug'
# errorlog = '%s/logs/%s_error.log' % (path, 'one')
# accesslog = '%s/logs/%s_access.log' % (path, 'one')
timeout = 3600
# -*- coding: utf-8 -*-
import os
import urllib
from utils.celery_tasks import app
from utils.conf import UPLOAD_FOLDER
import shutil


@app.task(time_limit=180, soft_time_limit=120, acks_late=True)
def task(url, _id):
    print 'ddd...', url.split('/')[-1], '---', _id
    filename_tmp = os.path.join(UPLOAD_FOLDER, _id + url.split('/')[-1] + '_tmp1')
    filename = os.path.join(UPLOAD_FOLDER, _id + url.split('/')[-1] + '_tmp')
    urllib.urlretrieve(url, filename_tmp)
    print 'over download %s' % filename_tmp
    shutil.move(filename_tmp, filename)
    return 'over...'
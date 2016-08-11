# -*- coding: utf-8 -*-
import os
import urllib
from utils.celery_tasks import app
from utils.conf import UPLOAD_FOLDER
import shutil
from utils.util import u_path


@app.task(acks_late=False)
def task(url, _id):
    print 'celery start...', url.split('/')[-1], '---', _id
    filename_tmp = u_path(os.path.join(UPLOAD_FOLDER, _id + url.split('/')[-1] + '_tmp1'))
    filename = u_path(os.path.join(UPLOAD_FOLDER, _id + url.split('/')[-1] + '_tmp'))
    urllib.urlretrieve(url, filename_tmp)
    print 'over download %s' % filename_tmp
    shutil.move(filename_tmp, filename)
    print 'over shift...'
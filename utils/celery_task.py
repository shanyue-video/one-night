# -*- coding: utf-8 -*-
import os
import urllib
from utils.celery_tasks import app
from utils.conf import UPLOAD_FOLDER


@app.task(time_limit=180, soft_time_limit=120, acks_late=True)
def task(url, _id):
    print 'ddd...', url.split('/')[-1], '---', _id
    filename = os.path.join(UPLOAD_FOLDER, _id + url.split('/')[-1] + '_tmp')
    urllib.urlretrieve(url, filename)
    print 'over download %s' % filename
    return 'over...'
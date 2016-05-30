# -*- coding: utf-8 -*-
import time
import boto3
import os
from utils.conf import UPLOAD_FOLDER

Bucket = 'one-night'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def loop():
    while True:
        for f in os.listdir(UPLOAD_FOLDER):
            f = f.decode('').encode('utf-8')
            if not 'tmp' == f.split('_')[-1]:
                continue
            else:
                print 'start handle %s' % f
                f_path = os.path.join(UPLOAD_FOLDER, f)
                f_path_new = os.path.join(UPLOAD_FOLDER, f[:-4])
                os.rename(f_path, f_path_new)
                s3_client = boto3.client('s3')
                s3_client.upload_file(f_path_new, Bucket, f[:-4])
                print 'end handle %s' % f[:-4]
                print time.strftime("%Y/%y/%d %H:%M:%S", time.localtime(time.time()))


if __name__ == '__main__':
    loop()
# -*- coding: utf-8 -*-
import os
from qiniu import Auth, put_file
from utils.conf import UPLOAD_FOLDER

access_key = '4vtH5Qbea2P_qbji0mkxAqjEr4oulloHX4yDgnJP'
secret_key = 'no0C1cbm0nv26_zvVr8PPgFo2HmNk0DPtr_aDDKJ'

bucket_name = 'one-night'

q = Auth(access_key, secret_key)

key = 'a'

token = q.upload_token(bucket_name, key, 3600)

local_file = os.path.join(UPLOAD_FOLDER, 'a')

ret, info = put_file(token, key, local_file)
print(info)


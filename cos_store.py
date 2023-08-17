"""
COS 存储使用demo: 

"""


from datetime import datetime, timedelta
from hashlib import sha1
import hmac

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError
from qcloud_cos import CosClientError

import sys, os
import logging

os.environ['DJANGO_SETTINGS_MODULE'] = 'tracker.settings'
from django.conf import settings

def percentage(consumed_bytes, total_bytes):
    """进度条回调函数，计算当前上传的百分比

    :param consumed_bytes: 已经上传/下载的数据量
    :param total_bytes: 总数据量
    """
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print("\r{0}% ".format(rate))
        sys.stdout.flush()


if __name__ == "__main__":

    config = CosConfig(
        Region=settings.COS_Region, SecretId=settings.COS_SECRETID, SecretKey=settings.COS_SECRETKEY
    )
    client = CosS3Client(config)
    bucket_name = "python-saas-1254172610"
    resp = client.upload_file(
        Bucket=bucket_name,
        LocalFilePath="/home/manhand/Pictures/1200x1200bf-60.jpg",
        Key="fuckyou.jpg",
        PartSize=10,
        MAXThread=5,
        progress_callback=percentage,
    )
    print(resp["ETag"])

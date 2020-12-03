# -*-coding:utf-8 -*-
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
import os
import time
import random
from data_deal import utils


class FileStorage(FileSystemStorage):
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        #初始化
        super(FileStorage, self).__init__(location, base_url)

    #重写 _save方法
    def _save(self, name, content):
        #文件扩展名
        ext = os.path.splitext(name)[1]
        #文件目录
        d = os.path.dirname(name)
        # 定义文件名，源文件名，避开系统定义的随机字符串追加，所以避开不用name字段
        end = utils.find_last(str(content), ".")
        filename = ""
        if end != -1:
            filename = str(content)[:end]
        # 定义文件名，年月日时分秒随机数
        fn = time.strftime("%Y%m%d%H%M%S")
        # fn = fn + "_%d" % random.randint(0, 100)
        #重写合成文件名
        name = os.path.join(d, filename + fn + ext)
        #调用父类方法
        return super(FileStorage, self)._save(name, content)

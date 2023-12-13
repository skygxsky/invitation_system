from __future__ import absolute_import, unicode_literals
import os
import django
from celery import Celery
from django.conf import settings


# 设置系统环境变量，安装django，必须设置，否则在启动celery时会报错
# django_celery_demo 是当前项目名
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitor_system.settings')
django.setup()

celery_app = Celery('monitor_system')
celery_app.config_from_object('django.conf:settings')
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

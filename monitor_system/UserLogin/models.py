from django.db import models

# Create your models here.


class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(verbose_name='昵称',max_length=32,default="")
    username = models.CharField(verbose_name='用户名',max_length=32,unique=True)
    password = models.CharField(verbose_name='密码',max_length=64)
    create_time = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
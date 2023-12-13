from django.db import models

# Create your models here.


class RunInfo(models.Model):
    """
    各平台运行信息
    """
    platform_name = models.CharField(verbose_name='平台名称',max_length=32,default="", unique=True)
    cookies = models.ForeignKey('PlatformCookies', on_delete=models.SET_NULL, null=True, blank=True, default=None)

    run_info_total = models.IntegerField('运行概览_总执行', default=0)
    run_info_running = models.IntegerField('运行概览_运行中', default=0)
    run_info_success = models.IntegerField('运行概览_成功', default=0)
    run_info_fail = models.IntegerField('运行概览_失败', default=0)
    run_info_error = models.IntegerField('运行概览_异常', default=0)

    case_info_case_count = models.IntegerField('用例概览_总数', default=0)
    case_info_alarming = models.IntegerField('用例概览_告警中', default=0)
    case_info_open_alarm = models.IntegerField('用例概览_开启告警', default=0)
    case_info_success = models.IntegerField('用例概览_成功', default=0)
    case_info_error = models.IntegerField('用例概览_异常', default=0)
    case_info_fail = models.IntegerField('用例概览_失败', default=0)

    plan_info_running = models.IntegerField('策略_运行中', default=0)
    plan_info_plan = models.IntegerField('策略_计划中', default=0)

    eu_info_online = models.IntegerField('主控_在线', default=0)
    eu_info_offline = models.IntegerField('主控_离线', default=0)

    device_info_online = models.IntegerField('设备_在线', default=0)
    device_info_offline = models.IntegerField('设备_离线', default=0)
    device_info_running = models.IntegerField('设备_运行中', default=0)

    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

class PlatformCookies(models.Model):
    """
    各平台crsfcookies
    """
    platform_cookies = models.CharField(verbose_name='平台cookies',max_length=128,default="")
    platform_url = models.CharField(verbose_name='平台url',max_length=128,default="")
    platform_name = models.CharField(verbose_name='平台名称',max_length=128,default="", unique=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

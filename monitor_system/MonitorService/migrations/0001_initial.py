# Generated by Django 4.1 on 2023-12-09 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RunInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(default='', max_length=32, verbose_name='平台名称')),
                ('run_info_total', models.IntegerField(default=0, verbose_name='运行概览_总执行')),
                ('run_info_running', models.IntegerField(default=0, verbose_name='运行概览_运行中')),
                ('run_info_success', models.IntegerField(default=0, verbose_name='运行概览_成功')),
                ('run_info_fail', models.IntegerField(default=0, verbose_name='运行概览_失败')),
                ('run_info_error', models.IntegerField(default=0, verbose_name='运行概览_异常')),
                ('case_info_case_count', models.IntegerField(default=0, verbose_name='用例概览_总数')),
                ('case_info_alarming', models.IntegerField(default=0, verbose_name='用例概览_告警中')),
                ('case_info_open_alarm', models.IntegerField(default=0, verbose_name='用例概览_开启告警')),
                ('case_info_success', models.IntegerField(default=0, verbose_name='用例概览_成功')),
                ('case_info_error', models.IntegerField(default=0, verbose_name='用例概览_异常')),
                ('case_info_fail', models.IntegerField(default=0, verbose_name='用例概览_失败')),
                ('plan_info_running', models.IntegerField(default=0, verbose_name='策略_运行中')),
                ('plan_info_plan', models.IntegerField(default=0, verbose_name='策略_计划中')),
                ('eu_info_online', models.IntegerField(default=0, verbose_name='主控_在线')),
                ('eu_info_offline', models.IntegerField(default=0, verbose_name='主控_离线')),
                ('device_info_online', models.IntegerField(default=0, verbose_name='设备_在线')),
                ('device_info_offline', models.IntegerField(default=0, verbose_name='设备_离线')),
                ('device_info_running', models.IntegerField(default=0, verbose_name='设备_运行中')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
        ),
    ]
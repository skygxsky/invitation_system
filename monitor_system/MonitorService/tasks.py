from celery import shared_task
from loguru import logger

from MonitorService.models import PlatformCookies, RunInfo
import requests


@shared_task
def request_run_info():
    platform_cookies_set = PlatformCookies.objects.values('platform_cookies', 'platform_url', 'platform_name')
    for i in platform_cookies_set:
        logger.debug(i['platform_name'])
        try:
            url = i['platform_url']
            platform_cookies = i['platform_cookies']
            platform_name = i['platform_name']
            response = requests.get(url, headers={
                'Cookie': 'sessionid={}'.format(platform_cookies)}).json()
            run_info_running = response['run_info']['running']
            run_info_success = response['run_info']['success']
            run_info_fail = response['run_info']['fail']
            run_info_error = response['run_info']['error']
            run_info_total = run_info_success + run_info_fail + run_info_error

            case_info_case_count = response['case_info']['case_count']
            case_info_alarming = response['case_info']['alarming']
            case_info_open_alarm = response['case_info']['open_alarm']
            case_info_success = response['case_info']['success']
            case_info_error = response['case_info']['error']
            case_info_fail = response['case_info']['fail']

            plan_info_running = response['plan_info']['running']
            plan_info_plan = response['plan_info']['plan']

            eu_info_online = response['eu_info']['online']
            eu_info_offline = response['eu_info']['offline']

            device_info_online = response['device_info']['online']
            device_info_offline = response['device_info']['offline']
            device_info_running = response['device_info']['running']

            RunInfo.objects.update_or_create(platform_name=platform_name,defaults={
                'run_info_total':run_info_total,'run_info_running':run_info_running,'run_info_success':run_info_success,
                'run_info_fail':run_info_fail,'run_info_error':run_info_error,'case_info_case_count':case_info_case_count,
                'case_info_alarming':case_info_alarming,'case_info_open_alarm':case_info_open_alarm,'case_info_success':case_info_success,
                'case_info_error':case_info_error,'case_info_fail':case_info_fail,'plan_info_running':plan_info_running,
                'plan_info_plan':plan_info_plan,'eu_info_online':eu_info_online,'eu_info_offline':eu_info_offline,
                'device_info_online':device_info_online,'device_info_offline':device_info_offline,'device_info_running':device_info_running
            })
        except Exception as e:
            logger.error(e)

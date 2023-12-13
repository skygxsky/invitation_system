from rest_framework.views import APIView
from rest_framework.response import Response
from loguru import logger
import datetime
from MonitorService.models import PlatformCookies,RunInfo
from UserLogin.utils.jwt_auth import create_token, JwtQueryParamsAuthentication


class MonitorInfo(APIView):
    """
    监控信息
    """

    # authentication_classes = [JwtQueryParamsAuthentication]

    def get(self,request,*args,**kwargs):
        info_set = RunInfo.objects.all().values()
        out_time = datetime.datetime.now() - datetime.timedelta(minutes=1)
        num = 0
        for i in info_set:
            if i['update_time'] >= out_time:
                i['out_time'] = True
                num += 1
            else:
                i['out_time'] = False
        return Response({
            'code': 20000,
            'data':{
                'total':len(info_set),
                'online':num,
                'items':info_set
            }
        })

    def post(self,request,*args,**kwargs):
        return Response({'code':20000})
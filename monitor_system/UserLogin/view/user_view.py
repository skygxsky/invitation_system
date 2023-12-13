from rest_framework.views import APIView
from rest_framework.response import Response
from loguru import logger

from UserLogin.models import UserInfo
from UserLogin.utils.jwt_auth import create_token, JwtQueryParamsAuthentication


class UserLogin(APIView):
    """
    app端用户登录
    """

    def post(self,request,*args,**kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user_object = UserInfo.objects.filter(username=username,password=password).first()
        if not user_object:
            return Response({
                'code': 0, 'token':'', 'msg': "用户名或密码错误",
            })
        token = create_token({
            'id': user_object.id,
            "name": user_object.username
        })
        return Response({'code': 20000, 'token':token, 'msg': "token获取成功",})

    def delete(self,request,*args,**kwargs):
        """
        退出登录
        """
        return Response({'code': 20000, 'data': 'success', })

class User(APIView):
    """
    用户信息
    """
    authentication_classes = [JwtQueryParamsAuthentication]

    def get(self,request,*args,**kwargs):
        return Response({
            "code": 20000,
            "data": {
                "roles": [
                    "admin"
                ],
                "introduction": "I am a super administrator",
                "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
                "name": "Monitor"
            }
        })

class Register(APIView):
    """
    用户注册
    """

    def post(self,request,*args,**kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        UserInfo.objects.create(username=username,password=password)
        return Response({
            'code': 20000,
            'msg': '成功'
        })



from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from api.utils.jwt_auth import create_token
from api.extensions.auth import JwtQueryParamsAuthentication
from api.myserialisers.myserializers import *
from api.myret.MyRet import *
from api.mypage.MyPage import *
from api.mypermission.MyPermission import *
from loguru import logger
import time,datetime

class UserLogin(APIView):
    """
    app端用户登录
    """

    def post(self,request,*args,**kwargs):
        ret = RET1
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user_object = models.UserInfo.objects.filter(username=username,password=password).first()
            if not user_object:
                ret["code"] = 1
                ret["msg"] = "用户名或密码错误"
                return Response(ret)
            token = create_token({
                'id': user_object.id,
                "name": user_object.username
            })
            ret["code"] = 0
            ret["data"]["token"] = token
            ret["msg"] = "登陆成功"
            return Response(ret)
        except:
            ret["code"] = 0
            ret["msg"] = '登陆失败'
            return Response(ret)

class GetUserInfo(APIView):
    """
    获取用户信息
    """
    authentication_classes = [JwtQueryParamsAuthentication,]

    def get(self,request,*args,**kwargs):
        ret = RET5
        try:
            id = request.user["id"]
            user = models.UserInfo.objects.filter(id=int(id)).first()
            content = models.UserInfo.objects.filter(id=int(id)).values()[0]
            ser = GetUserInfoSerializer(instance=user, context={'request': request})
            content["role"] = ",".join([i["title"] for i in ser.data["roles"]])
            del content["create_time"]
            del content["upload_time"]
            ret["code"] = 0
            ret["data"] = content
            ret["msg"] = "登录成功"
            return Response(ret)
        except:
            ret["code"] = 1
            return Response(ret)

class UserView(APIView):
    """
    用户注册
    """
    def post(self,request,*args,**kwargs):
        ret = RET5
        try:
            data = request.data
            models.UserInfo.objects.create(
                username=data["username"],
                password=data["password"],
                real_name=data["realname"],
                phone=data["phone"]
            )
            ret['code'] = 0
            ret['msg'] = "注册成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "注册失败"
            return Response(ret)

class PutUserView(APIView):
    """
    用户信息完善
    """
    authentication_classes = [JwtQueryParamsAuthentication,]

    def put(self,request,*args,**kwargs):
        ret = RET5
        try:
            user_id = request.user["id"]
            data = request.data
            gender = 0
            if data["gender"] == "女":
                gender = 1
            models.UserInfo.objects.filter(id=int(user_id)).update(
                nick=data["nick"],
                gender=gender,
                birthday=data["birthday"],
                city=data["city"],
                avatar=data["avatar"]
            )
            ret['code'] = 0
            ret['msg'] = "编辑成功"
            return Response(ret)
        except:
            ret['code'] = 0
            ret['msg'] = "编辑失败"
            return Response(ret)

class Picture(APIView):
    """
    图片上传
    """
    authentication_classes = [JwtQueryParamsAuthentication,]

    def post(self,request,*args,**kwargs):
        ret = RET5
        data = request.data

        return Response(ret)


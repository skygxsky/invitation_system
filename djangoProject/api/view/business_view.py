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

class PostCate(APIView):
    """
    帖子分类模块
    """
    authentication_classes = [JwtQueryParamsAuthentication]
    permission_classes = [SuperPermissions,]

    def get(self,request,*args,**kwargs):
        ret = RET7
        try:
            if request.query_params == {}:
                types = models.InvitationType.objects.all().values('id','type_title','type_desc')
                ret["code"] = 0
                ret["data"]["total"] = len(types)
                ret["data"]["category"] = types
                ret["msg"] = "获取成功"
                return Response(ret)
            else:
                types = models.InvitationType.objects.all()
                pg = MyPageNumberPagination()
                pager_roles = pg.paginate_queryset(queryset=types, request=request, view=self)
                ser = PagerInvitationTypeSerializers(instance=pager_roles, many=True)
                ret["code"] = 0
                ret["data"]["total"] = len(types)
                ret["data"]["category"] = ser.data
                ret["msg"] = "获取成功"
                return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "获取失败"
            return Response(ret)

    def post(self,request,*args,**kwargs):
        """
        帖子状态默认为关闭状态
        """
        ret = RET5
        try:
            data = request.data
            models.InvitationType.objects.create(
                type_title=data["cate_name"],
                type_desc=data["cate_desc"],
                status="关闭"
            )
            ret['code'] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)

    def delete(self,request,*args,**kwargs):
        ret = RET5
        try:
            data = request.data["id"]
            for i in data:
                models.InvitationType.objects.filter(id=int(i)).delete()
            ret["code"] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)

    def put(self,request,*args,**kwargs):
        ret = RET5
        try:
            data = request.data
            models.InvitationType.objects.filter(id=int(data["id"])).update(
                type_title=data["cate_name"],
                type_desc=data["cate_desc"]
            )
            ret["code"] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)

class SystemMessage(APIView):
    """
    系统通知模块
    """
    authentication_classes = [JwtQueryParamsAuthentication,]
    permission_classes = [SuperPermissions,]

    def get(self,request,*args,**kwargs):
        ret = RET8
        try:
            if request.query_params == {}:
                notices = models.SystemNotice.objects.all().values('id','sn_content','not_range','status','start_time','end_time')
                ret["code"] = 0
                ret["data"]["total"] = len(notices)
                ret["data"]["notices"] = notices
                ret["msg"] = "获取成功"
                return Response(ret)
            else:
                notices = models.SystemNotice.objects.all()
                pg = MyPageNumberPagination()
                pager_notices = pg.paginate_queryset(queryset=notices,request=request,view=self)
                ser = PagerSystemNoticeSerializers(instance=pager_notices,many=True)
                ret["code"] = 0
                ret["data"]["total"] = len(notices)
                ret["data"]["notices"] = ser.data
                ret["msg"] = "获取成功"
                return Response(ret)
        except:
            ret['code'] = 1
            ret['msg'] = "获取失败"
            return Response(ret)

    def post(self,request,*args,**kwargs):
        """
        status默认为0
        """
        ret = RET5
        try:
            data = request.data
            models.SystemNotice.objects.create(
                sn_content=data["sysMesContext"],
                not_range=data["sysMesScope"],
                status=0,
                start_time=data["startTime"],
                end_time=data["endTime"]
            )
            ret["code"] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)

    def put(self,request,*args,**kwargs):
        ret = RET5
        try:
            notice_id = request.data["id"]
            status = models.SystemNotice.objects.filter(id=int(notice_id)).values("status").first()
            if int(status["status"]) == 0:
                models.SystemNotice.objects.filter(id=int(notice_id)).update(status=1)
            else:
                models.SystemNotice.objects.filter(id=int(notice_id)).update(status=0)
            ret["code"] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)

    def delete(self,request,*args,**kwargs):
        ret = RET5
        data = request.data
        try:
            for i in data["id"]:
                models.SystemNotice.objects.filter(id=int(i)).delete()
            ret["code"] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)

class Ad(APIView):
    """
    广告管理模块
    """
    authentication_classes = [JwtQueryParamsAuthentication,]
    permission_classes = [SuperPermissions,]

    def get(self,request,*args,**kwargs):
        ret = RET9
        try:
            if request.query_params == {}:
                ads = models.Advertisement.objects.all().values('id','advertising_space','advertising_img','advertising_url','enable_time','end_time','status','flow')
                ret["code"] = 0
                ret["data"]["total"] = len(ads)
                ret["data"]["roles"] = ads
                ret["msg"] = "获取成功"
                return Response(ret)
            else:
                ads = models.Advertisement.objects.all()
                pg = MyPageNumberPagination()
                pager_ads = pg.paginate_queryset(queryset=ads,request=request,view=self)
                ser = PagerAdvertisementSerializers(instance=pager_ads,many=True)
                ret["code"] = 0
                ret["data"]["total"] = len(ads)
                ret["data"]["roles"] = ser.data
                ret["msg"] = "获取成功"
                return Response(ret)
        except:
            ret['code'] = 1
            ret['msg'] = "获取失败"
            return Response(ret)

    def post(self,request,*args,**kwargs):
        """
        广告状态默认为0
        """
        ret = RET5
        try:
            data = request.data
            models.Advertisement.objects.create(
                advertising_space=data["adSpace"],
                advertising_img=data["adImg"],
                advertising_url=data["adUrl"],
                enable_time=data["startTime"],
                end_time=data["endTime"],
                status=0,
                flow=0
            )
            ret["code"] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)

    def put(self,request,*args,**kwargs):
        ret = RET5
        try:
            data = request.data
            models.Advertisement.objects.filter(advertising_space=data["adSpace"]).update(
                advertising_space=data["adSpace"],
                advertising_img=data["adImg"],
                advertising_url=data["adUrl"],
                enable_time=data["startTime"],
                end_time=data["endTime"],
            )
            ret["code"] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)

    def delete(self,request,*args,**kwargs):
        ret = RET5
        try:
            data = request.data
            for i in data["id"]:
                models.Advertisement.objects.filter(id=int(i)).delete()
            ret["code"] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)

class UpdateStatus(APIView):
    """
    若开启时间未到达被开启，则将会默认将开启时间设置为转化时间
    """
    authentication_classes = [JwtQueryParamsAuthentication,]
    permission_classes = [SuperPermissions,]

    def put(self,request,*args,**kwargs):
        ret = RET5
        try:
            data = request.data
            now = time.localtime(int(time.time()))
            times = time.strftime("%Y-%m-%d", now)
            models.Advertisement.objects.filter(id=int(data["id"])).update(
                enable_time=times,
                status=1
            )
            ret["code"] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)



















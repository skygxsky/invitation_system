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

class LoginView(APIView):
    """
    用户登录
    """
    def post(self,request):
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
    登录，获取个人真实姓名
    """
    authentication_classes = [JwtQueryParamsAuthentication,]
    permission_classes = [SuperPermissions,]

    def get(self,request,*args,**kwargs):
        ret = RET2
        try:
            username = request.user["name"]
            id = request.user["id"]
            user = models.UserInfo.objects.filter(username=username).first()
            ser = GetUserInfoSerializer(instance=user,context={'request': request})
            ret["code"] = 0
            ret["data"]["id"] = id
            ret["data"]["real_name"] = ser.data["real_name"]
            ret["data"]["role"] = ",".join([i["title"] for i in ser.data["roles"]])
            ret["msg"] = "登录成功"
            return Response(ret)
        except:
            ret["code"] = 1
            return Response(ret)

class GetRouter(APIView):
    """
    获取用户权限表
    """
    authentication_classes = [JwtQueryParamsAuthentication,]
    permission_classes = [SuperPermissions, ]

    def get(self,request,*args,**kwargs):
        ret = RET3
        try:
            username = request.user["name"]
            user = models.UserInfo.objects.filter(username=username).first()
            user_ser = GetUserInfoSerializer(instance=user, context={'request': request})
            role_title = user_ser.data["roles"][0]["title"]# 角色
            routes = models.Role.objects.filter(title=role_title)
            permissions_ser = GetRouterSerializer(instance=routes,many=True,context={'request': request})
            parents_list = []  # 父级
            children_list = []  # 子级
            for i in permissions_ser.data[0]["permissions"]:
                if i["parents_id"] == 0:
                    i["children"] = []
                    del i["create_time"]
                    del i["upload_time"]
                    parents_list.append(i)
                else:
                    children_list.append(i)
            for j in children_list:
                del j["create_time"]
                del j["upload_time"]
                for q in parents_list:
                    if j["parents_id"] == q["id"]:
                        q["children"].append(j)
            # while children_list:
            #     p = children_list.pop()
            #     del p["create_time"]
            #     del p["upload_time"]
            #     for j in parents_list:
            #         if j["id"] == p["parents_id"]:
            #             j["children"].append(p)
            #         else:
            #             result_list.append(j)
            ret["code"] = 0
            ret["data"]["router"] = parents_list
            ret["msg"] = "登录成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "登陆失败"
            return Response(ret)

class Admin(APIView):
    """
    后台账号管理模块
    """
    authentication_classes = [JwtQueryParamsAuthentication,]
    permission_classes = [SuperPermissions, ]


    def get(self,request,*args,**kwargs):
        ret = RET4
        try:
            if request.query_params == {}:
                userinfo = models.UserInfo.objects.all()
                ser = GetUserInfoSerializer(instance=userinfo,many=True)
                list1 = []
                list2 = []
                for i in ser.data:
                    del i["create_time"]
                    del i["upload_time"]
                    rid = i["roles"][0]["id"]
                    role = i["roles"][0]["title"]
                    del i["roles"]
                    i["rid"] = rid
                    i["role"] = role
                    list1.append(i)
                for j in list1:
                    if int(j["id"]) == int(request.user["id"]):
                        del j
                    elif j["role"] == "普通用户":
                        del j
                    else:
                        list2.append(j)
                ret["code"] = 0
                ret["data"]["total"] = len(userinfo)
                ret["data"]["account"] = list2
                ret["msg"] = "获取成功"
                return Response(ret)
            else:
                userinfo = models.UserInfo.objects.all()
                pg = MyPageNumberPagination()
                pager_roles = pg.paginate_queryset(queryset=userinfo,request=request,view=self)
                ser = GetUserInfoSerializer(instance=pager_roles,many=True)
                list1 = []
                for i in ser.data:
                    del i["create_time"]
                    del i["upload_time"]
                    rid = i["roles"][0]["id"]
                    role = i["roles"][0]["title"]
                    del i["roles"]
                    i["rid"] = rid
                    i["role"] = role
                    list1.append(i)
                ret["code"] = 0
                ret["data"]["total"] = len(userinfo)
                ret["data"]["account"] = list1
                ret["msg"] = "获取成功"
                return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "获取失败"
            return Response(ret)

    def post(self,request,*args,**kwargs):
        ret = RET5
        try:
            data = request.data
            if data["rid"]:
                models.UserInfo.objects.create(
                    username=data["username"],
                    password=data["password"],
                    real_name=data["real_name"]
                )
                obj = models.UserInfo.objects.filter(username=data["username"]).first()
                obj.roles.add(int(data["rid"]))
                ret["code"] = 0
                ret["msg"] = "添加角色操作成功"
                return Response(ret)
            else:
                models.UserInfo.objects.create(
                    username=data["username"],
                    password=data["password"],
                    real_name=data["real_name"]
                )
                ret["code"] = 0
                ret["msg"] = "添加账户操作成功"
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
                models.UserInfo.objects.filter(id=int(i)).delete()
            ret["code"] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)

class ResetRole(APIView):
    """
    分配权限
    """
    authentication_classes = [JwtQueryParamsAuthentication,]
    permission_classes = [SuperPermissions, ]

    def put(self,request,*args,**kwargs):
        ret = RET5
        try:
            data = request.data
            user_id = data["id"]
            role_id = data["rid"]
            obj = models.UserInfo.objects.filter(id=user_id).first()
            old_role_id = obj.roles.all().values()[0]["id"]
            obj.roles.remove(int(old_role_id))
            obj.roles.add(int(role_id))
            ret["code"] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)

class ResetPassword(APIView):
    """
    重置账户密码（默认重置为123456）
    """
    authentication_classes = [JwtQueryParamsAuthentication,]
    permission_classes = [SuperPermissions, ]

    def put(self,request,*args,**kwargs):
        ret = RET5
        try:
            userinfo_id = request.data["id"]
            models.UserInfo.objects.filter(id=int(userinfo_id)).update(password="123456")
            ret["code"] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)

class Roles(APIView):
    """
    角色管理模块
    """
    authentication_classes = [JwtQueryParamsAuthentication,]
    permission_classes = [SuperPermissions, ]

    def get(self,request,*args,**kwargs):
        ret = RET6
        data = request.query_params
        try:
            if data == {}:
                roles = models.Role.objects.all().values("id","title",'r_desc')
                list1 = []
                for i in roles:
                    if i["title"] == '超级管理员':
                        del i
                    else:
                        list1.append(i)
                ret["code"] = 0
                ret["data"]["total"] = len(roles)
                ret["data"]["roles"] = list1
                ret["msg"] = "获取成功"
                return Response(ret)
            elif data["r_name"]:
                roles = models.Role.objects.filter(title__contains=data["r_name"])
                pg = MyPageNumberPagination()
                pager_roles = pg.paginate_queryset(queryset=roles, request=request, view=self)
                ser = PagerRoleSerializers(instance=pager_roles, many=True)
                list1 = []
                for i in ser.data:
                    if i["title"] == '超级管理员':
                        del i
                    else:
                        list1.append(i)
                ret["code"] = 0
                ret["data"]["total"] = len(roles)
                ret["data"]["roles"] = list1
                ret["msg"] = "获取成功"
                return Response(ret)
            else:
                roles = models.Role.objects.all()
                pg = MyPageNumberPagination()
                pager_roles = pg.paginate_queryset(queryset=roles,request=request,view=self)
                ser = PagerRoleSerializers(instance=pager_roles,many=True)
                list1 = []
                for i in ser.data:
                    if i["title"] == '超级管理员':
                        del i
                    else:
                        list1.append(i)
                ret["code"] = 0
                ret["data"]["total"] = len(roles)
                ret["data"]["roles"] = list1
                ret["msg"] = "获取成功"
                return Response(ret)
        except:
            ret['code'] = 1
            ret['msg'] = "获取失败"
            return Response(ret)

    def post(self,request,*args,**kwargs):
        ret = RET5
        try:
            title = request.data["r_name"]
            r_desc = request.data["r_desc"]
            models.Role.objects.create(title=title,r_desc=r_desc)
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
            id = request.data["id"]
            r_name = request.data["r_name"]
            r_desc = request.data["r_desc"]
            models.Role.objects.filter(id=int(id)).update(title=r_name,r_desc=r_desc)
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
                models.Role.objects.filter(id=int(i)).delete()
            ret["code"] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)

class Permission(APIView):
    """
    分配给角色路由权限
    """
    authentication_classes = [JwtQueryParamsAuthentication,]
    permission_classes = [SuperPermissions, ]

    def post(self,request,*args,**kwargs):
        ret = RET5
        try:
            role_id = request.data["id"]
            rid_list = request.data["rid"]
            obj = models.Role.objects.filter(id=int(role_id)).first()
            obj.permissions.clear()
            for i in rid_list:
                obj.permissions.add(int(i))
            ret["code"] = 0
            ret["msg"] = "操作成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "操作失败"
            return Response(ret)

class GetPowerTree(APIView):
    """
    id看路由
    """
    authentication_classes = [JwtQueryParamsAuthentication,]
    permission_classes = [SuperPermissions,]

    def get(self,request,*args,**kwargs):
        ret = RET3
        try:
            role_id = request.query_params["id"]
            routes = models.Role.objects.filter(id=int(role_id))
            permissions_ser = GetRouterSerializer(instance=routes, many=True, context={'request': request})
            parents_list = []  # 父级
            children_list = []  # 子级
            for i in permissions_ser.data[0]["permissions"]:
                if i["parents_id"] == 0:
                    i["children"] = []
                    del i["create_time"]
                    del i["upload_time"]
                    parents_list.append(i)
                else:
                    children_list.append(i)
            for j in children_list:
                del j["create_time"]
                del j["upload_time"]
                for q in parents_list:
                    if j["parents_id"] == q["id"]:
                        q["children"].append(j)
            ret["code"] = 0
            ret["data"]["router"] = parents_list
            ret["msg"] = "登录成功"
            return Response(ret)
        except:
            ret["code"] = 1
            ret["msg"] = "登陆失败"
            return Response(ret)






class AddModels(APIView):
    """
    增加数据表数据 测试用
    """
    def get(self,request,*args,**kwargs):
        # obj = models.UserInfo.objects.filter(id=2).first()
        # obj.roles.add(2)
        # models.UserInfo.objects.create(
        #     username="user1",
        #     password="123",
        #     real_name="龙哥"
        # )
        # models.Role.objects.create(
        #     title="一级管理员"
        # )
        # obj = models.UserInfo.objects.filter(id=2).first()
        # obj = models.Role.objects.filter(id=1).first()
        # # # print([i for i in range(1,31)])
        # obj.permissions.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)
        # obj.permissions.add(*[tuple(i) for i in range(31)])
        # import pandas as pd
        #
        # df = pd.read_excel("路由表设计.xlsx")
        # dicts = df.to_dict(orient='records')
        # lists = []
        # for i in dicts:
        #     if i["是否隐藏路由"] == False:
        #         i["是否隐藏路由"] = 1
        #         lists.append(i)
        #     else:
        #         i["是否隐藏路由"] = 2
        #         lists.append(i)
        # for j in lists:
        #     models.Permission.objects.create(
        #         route_url="%s"%(j["路由路径"]),
        #         route_name="%s"%(j["路由名称"]),
        #         route_title="%s"%(j["路由标题"]),
        #         route_hide="%s"%(j["是否隐藏路由"]),
        #         parents_id="%s"%(j["父路由id"])
        #     )
        models.InvitationType.objects.create(
            type_title="修真",
            type_desc="求得真我，去伪存真",
            status="仙境"
        )


        return Response("保存成功")



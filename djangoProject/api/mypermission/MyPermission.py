from rest_framework.permissions import BasePermission
from api import models
from api.myserialisers.myserializers import *

class SuperPermissions(BasePermission):
    def has_permission(self, request, view):
        try:
            role_id = request.user["id"]
            user = models.UserInfo.objects.filter(id=int(role_id))
            ser = GetUserInfoSerializer(instance=user,many=True,context={'request': request})
            title = ser.data[0]["roles"][0]["title"]
            if title == "超级管理员":
                return True
            return False
        except:
            return False
"""
序列化
"""
from rest_framework import serializers
from api import models

class GetUserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserInfo
        fields = "__all__"
        depth = 1

class GetRouterSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Role
        fields = "__all__"
        depth = 1

class PagerUserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = ["id","real_name","username"]

class PagerRoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = ["id","title","r_desc"]

class PagerInvitationTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.InvitationType
        fields = ['id','type_title','type_desc']

class PagerSystemNoticeSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.SystemNotice
        fields = ['id','sn_content','not_range','status','start_time','end_time']

class PagerAdvertisementSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Advertisement
        fields = ['id','advertising_space','advertising_img','advertising_url','enable_time','end_time','status','flow']



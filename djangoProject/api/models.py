from django.db import models

# Create your models here.

class Permission(models.Model):
    """
    权限表
    """
    hide_type_choices = (
        (1, 'FALSE'),
        (2, 'TRUE'),

    )
    route_url = models.CharField(max_length=64, verbose_name="路由路径", unique=True)
    route_name = models.CharField(max_length=32, verbose_name="路由名称")
    route_title = models.CharField(max_length=32, verbose_name="路由标题")
    route_hide = models.IntegerField(choices=hide_type_choices)
    parents_id = models.IntegerField()
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True,blank=True,null=True)#添加时的时间，更新对象时不会有变动。
    upload_time = models.DateTimeField(verbose_name='更新时间',auto_now=True,null=True,blank=True)#无论是你添加还是修改对象，时间为你添加或者修改的时间。

    def __str__(self):
        return self.route_title
class Role(models.Model):
    """
    角色表
    """
    title = models.CharField(verbose_name='角色名称',max_length=32,unique=True)
    # 自建第三张表参数through='表名字',througth_fields=('列名','xx')
    r_desc = models.CharField(verbose_name='角色描述',max_length=64,blank=True)
    permissions = models.ManyToManyField(verbose_name='拥有的所有权限',to='Permission',blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True,null=True,blank=True)  # 添加时的时间，更新对象时不会有变动。
    upload_time = models.DateTimeField(verbose_name='更新时间', auto_now=True,null=True,blank=True)  # 无论是你添加还是修改对象，时间为你添加或者修改的时间。

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """
    用户表
    """
    gender_type_choice = (
        (0,"男"),
        (1,"女"),
    )
    real_name = models.CharField(verbose_name='昵称',max_length=32,default="")
    username = models.CharField(verbose_name='用户名',max_length=32,unique=True)
    password = models.CharField(verbose_name='密码',max_length=64)
    nick = models.CharField(max_length=64,verbose_name="昵称",blank=True,null=True)
    gender = models.IntegerField(choices=gender_type_choice,blank=True,null=True)
    birthday = models.CharField(max_length=32,verbose_name="生日",null=True,blank=True)
    city = models.CharField(max_length=32,verbose_name="现居城市",null=True,blank=True)
    avatar = models.TextField(verbose_name="头像地址",null=True,blank=True)
    phone = models.IntegerField(verbose_name="手机号",null=True,blank=True)
    vertify = models.IntegerField(verbose_name="验证码",null=True,blank=True)

    roles = models.ManyToManyField(verbose_name='拥有所以的角色',to='Role',blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True,null=True,blank=True)  # 添加时的时间，更新对象时不会有变动。
    upload_time = models.DateTimeField(verbose_name='更新时间', auto_now=True,null=True,blank=True)  # 无论是你添加还是修改对象，时间为你添加或者修改的时间。

    def __str__(self):
        return self.real_name

#==============================================================================================================
class InvitationType(models.Model):
    """
    帖子分类表
    """
    type_title = models.CharField(max_length=32,unique=True,verbose_name="分类名称")
    type_desc = models.CharField(max_length=128,verbose_name="分类描述")
    status = models.CharField(max_length=64,verbose_name="分类状态")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, null=True,
                                       blank=True)  # 添加时的时间，更新对象时不会有变动。
    upload_time = models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True,
                                       blank=True)  # 无论是你添加还是修改对象，时间为你添加或者修改的时间。

    def __str__(self):
        return self.type_title


class Invitation(models.Model):
    """
    帖子表
    """
    type_choices = (
        (0, "是"),
        (1, "否"),
    )
    invitation_title = models.CharField(max_length=64,unique=True,verbose_name="帖子标题")
    invitation_content = models.TextField(verbose_name="文字内容")
    invitation_type = models.CharField(max_length=32,verbose_name="帖子类型")
    invitation_label = models.CharField(max_length=64,verbose_name="帖子标签")
    page_views = models.PositiveIntegerField(verbose_name="浏览量")
    user_id = models.IntegerField(verbose_name="创建人id")
    top = models.IntegerField(choices=type_choices,verbose_name="是否置顶")
    cream = models.IntegerField(choices=type_choices,verbose_name="是否精华")
    recommend = models.IntegerField(choices=type_choices,verbose_name="是否推荐")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, null=True,
                                       blank=True)  # 添加时的时间，更新对象时不会有变动。
    upload_time = models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True,
                                       blank=True)  # 无论是你添加还是修改对象，时间为你添加或者修改的时间。

    def __str__(self):
        return self.invitation_title

class InvitationImg(models.Model):
    """
    帖子图片表
    """
    img_url = models.TextField(verbose_name="图片路径")
    img_content = models.TextField(verbose_name="图片内容")
    news = models.ForeignKey(verbose_name="帖子id",to="Invitation",on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, null=True,
                                       blank=True)  # 添加时的时间，更新对象时不会有变动。
    upload_time = models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True,
                                       blank=True)  # 无论是你添加还是修改对象，时间为你添加或者修改的时间。

    def __str__(self):
        return self.img_content

class Comment(models.Model):
    """
    评论表
    """
    news = models.ForeignKey(verbose_name="帖子id",to="Invitation",on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=255,verbose_name="回复内容")
    user_id = models.ForeignKey(verbose_name="评论者id",to="UserInfo",on_delete=models.CASCADE)

    reply = models.ForeignKey(verbose_name="回复",to="self",null=True,blank=True,on_delete=models.CASCADE,related_name="replys")
    depth = models.PositiveIntegerField(verbose_name="评论层级",default=1)
    root = models.ForeignKey(verbose_name="根评论",to="self",null=True,blank=True,on_delete=models.CASCADE,related_name="roots")

    # favor_count = models.PositiveIntegerField(verbose_name="赞数",default=0)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, null=True,
                                       blank=True)  # 添加时的时间，更新对象时不会有变动。
    upload_time = models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True,
                                       blank=True)  # 无论是你添加还是修改对象，时间为你添加或者修改的时间。

    def __str__(self):
        return self.comment_content

class Notice(models.Model):
    """
    聊天室公告表
    """
    notice_content = models.TextField(verbose_name="公告内容")
    status = models.CharField(max_length=64)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, null=True,
                                       blank=True)  # 添加时的时间，更新对象时不会有变动。
    upload_time = models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True,
                                       blank=True)  # 无论是你添加还是修改对象，时间为你添加或者修改的时间。

    def __str__(self):
        return self.notice_content

class ForbiddenLexicon(models.Model):
    """
    违禁词库
    """
    name = models.CharField(max_length=64,verbose_name="违禁词名称",unique=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, null=True,
                                       blank=True)  # 添加时的时间，更新对象时不会有变动。
    upload_time = models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True,
                                       blank=True)  # 无论是你添加还是修改对象，时间为你添加或者修改的时间。

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    """
    广告表
    """
    advertising_space = models.CharField(max_length=64,verbose_name="广告位")
    advertising_img = models.TextField(verbose_name="广告图片")
    advertising_url = models.TextField(verbose_name="广告链接")
    enable_time = models.DateField(verbose_name="启用时间")
    end_time = models.DateField(verbose_name="结束时间")
    status = models.CharField(max_length=64,verbose_name="广告状态")
    flow = models.PositiveIntegerField(verbose_name="广告流量")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, null=True,
                                       blank=True)  # 添加时的时间，更新对象时不会有变动。
    upload_time = models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True,
                                       blank=True)  # 无论是你添加还是修改对象，时间为你添加或者修改的时间。

    def __str__(self):
        return self.advertising_space

class SystemNotice(models.Model):
    """
    系统通知表
    """
    sn_content = models.TextField(verbose_name="通知内容")
    not_range = models.TextField(verbose_name="通知范围")
    status = models.CharField(max_length=64,verbose_name="状态")
    start_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, null=True,
                                       blank=True)  # 添加时的时间，更新对象时不会有变动。
    end_time = models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True,
                                       blank=True)  # 无论是你添加还是修改对象，时间为你添加或者修改的时间。

    def __str__(self):
        return self.sn_content

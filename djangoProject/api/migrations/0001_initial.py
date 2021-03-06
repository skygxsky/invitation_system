# Generated by Django 3.1.4 on 2020-12-08 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertising_space', models.CharField(max_length=64, verbose_name='广告位')),
                ('advertising_img', models.TextField(verbose_name='广告图片')),
                ('advertising_url', models.TextField(verbose_name='广告链接')),
                ('enable_time', models.DateField(verbose_name='启用时间')),
                ('end_time', models.DateField(verbose_name='结束时间')),
                ('status', models.CharField(max_length=64, verbose_name='广告状态')),
                ('flow', models.PositiveIntegerField(verbose_name='广告流量')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('upload_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='ForbiddenLexicon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='违禁词名称')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('upload_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitation_title', models.CharField(max_length=64, unique=True, verbose_name='帖子标题')),
                ('invitation_content', models.TextField(verbose_name='文字内容')),
                ('invitation_type', models.CharField(max_length=32, verbose_name='帖子类型')),
                ('invitation_label', models.CharField(max_length=64, verbose_name='帖子标签')),
                ('page_views', models.PositiveIntegerField(verbose_name='浏览量')),
                ('user_id', models.IntegerField(verbose_name='创建人id')),
                ('top', models.IntegerField(choices=[(0, '是'), (1, '否')], verbose_name='是否置顶')),
                ('cream', models.IntegerField(choices=[(0, '是'), (1, '否')], verbose_name='是否精华')),
                ('recommend', models.IntegerField(choices=[(0, '是'), (1, '否')], verbose_name='是否推荐')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('upload_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='InvitationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_title', models.CharField(max_length=32, unique=True, verbose_name='分类名称')),
                ('type_desc', models.CharField(max_length=128, verbose_name='分类描述')),
                ('status', models.CharField(max_length=64, verbose_name='分类状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('upload_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_content', models.TextField(verbose_name='公告内容')),
                ('status', models.CharField(max_length=64)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('upload_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_url', models.CharField(max_length=64, unique=True, verbose_name='路由路径')),
                ('route_name', models.CharField(max_length=32, verbose_name='路由名称')),
                ('route_title', models.CharField(max_length=32, verbose_name='路由标题')),
                ('route_hide', models.IntegerField(choices=[(1, 'FALSE'), (2, 'TRUE')])),
                ('parents_id', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('upload_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='角色名称')),
                ('r_desc', models.CharField(blank=True, max_length=64, verbose_name='角色描述')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('upload_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('permissions', models.ManyToManyField(blank=True, to='api.Permission', verbose_name='拥有的所有权限')),
            ],
        ),
        migrations.CreateModel(
            name='SystemNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn_content', models.TextField(verbose_name='通知内容')),
                ('not_range', models.TextField(verbose_name='通知范围')),
                ('status', models.CharField(max_length=64, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('upload_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(default='', max_length=32, verbose_name='昵称')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('upload_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('roles', models.ManyToManyField(blank=True, to='api.Role', verbose_name='拥有所以的角色')),
            ],
        ),
        migrations.CreateModel(
            name='InvitationImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.TextField(verbose_name='图片路径')),
                ('img_content', models.TextField(verbose_name='图片内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('upload_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.invitation', verbose_name='帖子id')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=255, verbose_name='回复内容')),
                ('depth', models.PositiveIntegerField(default=1, verbose_name='评论层级')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('upload_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.invitation', verbose_name='帖子id')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replys', to='api.comment', verbose_name='回复')),
                ('root', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roots', to='api.comment', verbose_name='根评论')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userinfo', verbose_name='评论者id')),
            ],
        ),
    ]

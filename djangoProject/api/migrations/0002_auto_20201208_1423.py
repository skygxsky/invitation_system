# Generated by Django 3.1.4 on 2020-12-08 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='systemnotice',
            old_name='upload_time',
            new_name='end_time',
        ),
    ]

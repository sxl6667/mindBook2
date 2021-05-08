# Generated by Django 3.2 on 2021-05-08 03:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(help_text='账户的唯一标识', verbose_name='账户id')),
                ('name', models.CharField(default='匿名用户', help_text='只允许8位字符', max_length=8, verbose_name='用户昵称')),
                ('pwd', models.CharField(help_text='这是用户密码', max_length=16, verbose_name='用户的密码')),
                ('sex', models.BooleanField(default=True, help_text='1为男，0为女', verbose_name='用户性别')),
                ('sign', models.CharField(default='', help_text='字符串', max_length=32, verbose_name='用户简短的签名')),
                ('poster', models.ImageField(default='', help_text='一个图片路径', upload_to='lsrc', verbose_name='用户的头像')),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('mod_date', models.DateTimeField(auto_now=True, help_text='用来回溯', verbose_name='每次更新时间')),
                ('level', models.BooleanField(default=False, verbose_name='用户是否有管理员权限')),
            ],
        ),
    ]

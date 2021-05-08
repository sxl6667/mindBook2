from django.db import models
import django.utils.timezone as timezone
import inspect
from app01 import models as mo
import collections
from functools import wraps


# Create your models here.
class User(models.Model):
    """账号表"""
    uid = models.CharField(max_length=64, verbose_name='账户id', help_text='可以是邮箱')
    pwd = models.CharField(max_length=64, verbose_name='账户密码')


class UserInfo(models.Model):
    """个人信息表"""
    name = models.CharField(max_length=32, verbose_name='账户姓名', default='匿名用户')
    sex = models.BooleanField(verbose_name='账户性别', help_text='false为女，Ture为男', default=True)
    sign = models.TextField(verbose_name='账户个性前面', default='')
    uid = models.IntegerField(verbose_name='账户id')
    poster = models.IntegerField(verbose_name='账户头像', default=0)
    date = models.DateTimeField(verbose_name='账户创建时间', default=timezone.now)
    update = models.DateTimeField(verbose_name='账户内容更新时间', auto_now=True)


class UserOf(models.Model):
    """个人关系表"""
    uid = models.IntegerField(verbose_name='用户')
    pid = models.IntegerField(verbose_name='所属模块')
    type = models.IntegerField(verbose_name='所属模块')


class Learn(models.Model):
    """学习计划表"""
    parent = models.IntegerField(verbose_name='父节点', help_text='父节点为0则是根节点', default=0)
    order = models.IntegerField(verbose_name='该父节点下的第几位', default=0)
    title = models.CharField(max_length=32, verbose_name='标题', default='一个新节点')
    section = models.BooleanField(default=False, verbose_name='该项下是否有文章')
    detail = models.TextField(verbose_name='该项的详细解释', default='')
    date = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    update = models.DateTimeField(verbose_name='每次更新时间', auto_now=True)


class SectionOf(models.Model):
    """文章关系表"""
    uid = models.IntegerField(verbose_name='所属学习计划')
    pid = models.IntegerField(verbose_name='文章id')


class Section(models.Model):
    """文章表"""
    title = models.CharField(max_length=32, verbose_name='文章标题', default='一个新的文章')
    detail = models.TextField(verbose_name='文章内容', default='')
    date = models.DateTimeField(verbose_name='文章创建时间', default=timezone.now)
    update = models.DateTimeField(verbose_name='文章更新时间', auto_now=True)


class Thinking(models.Model):
    """想法表"""
    title = models.CharField(max_length=32, verbose_name='文章标题', default='一个新的想法')
    detail = models.TextField(verbose_name='文章内容', default='')
    date = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    update = models.DateTimeField(verbose_name='文章更新时间', auto_now=True)


class Album(models.Model):
    """相册表"""
    title = models.CharField(max_length=32, verbose_name='相册标题', default='一个新的相册')
    detail = models.CharField(max_length=64, verbose_name='这个相册的详细介绍', default='')
    poster = models.IntegerField(verbose_name='相册封面')
    date = models.DateTimeField(verbose_name='相册创建时间', default=timezone.now)
    update = models.DateTimeField(verbose_name='相册更新时间', auto_now=True)


class Picture(models.Model):
    """图片表"""
    title = models.CharField(max_length=32, verbose_name='图片标题', default='一个新图片')
    detail = models.CharField(max_length=64, verbose_name='图片备注', default='')
    date = models.DateTimeField(verbose_name='图片上传时间', default=timezone.now)
    src = models.ImageField(verbose_name='图片路径', upload_to='picture')


class PictureOf(models.Model):
    """图片关系表"""
    uid = models.IntegerField(verbose_name='图片路径')
    pid = models.IntegerField(verbose_name='图片id')
    type = models.IntegerField(verbose_name='所属模组')


class File(models.Model):
    """文件表"""
    title = models.CharField(max_length=32, verbose_name='文件标题', default='一个新文件')
    poster = models.IntegerField(verbose_name='该资源封面')
    src = models.FileField(verbose_name='文件路径', upload_to='File')
    date = models.DateTimeField(verbose_name='文件上传时间', default=timezone.now)


class Navigation(models.Model):
    """导航表"""
    title = models.CharField(max_length=32, verbose_name='我的API，或者我的导航', default='一个新的API')
    src = models.TextField(verbose_name='API路径')
    date = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    update = models.DateTimeField(verbose_name='更新时间', auto_now=True)


class Label(models.Model):
    """标签表"""
    title = models.CharField(max_length=64, verbose_name='标签', default='一个新的标签')
    date = models.DateTimeField(verbose_name='标签创建时间', default=timezone.now)


class LabelOf(models.Model):
    """标签关系表"""
    uid = models.IntegerField(verbose_name='所属用户')
    pid = models.IntegerField(verbose_name='所属模块')
    type = models.IntegerField(verbose_name='模块类型')
    lid = models.IntegerField(verbose_name='标签')


clsmember = inspect.getmembers(mo, inspect.isclass)
# print(clsmember)
#
# Mymodel = collections.namedtuple('Mymodel', ('model', 'this_id'))
#
# class MyModel:
#     def __init__(self, ):
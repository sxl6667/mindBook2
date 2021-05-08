from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class User(models.Model):
    """
    用户表
    """
    uid = models.IntegerField(verbose_name='账户id', help_text='账户的唯一标识')
    name = models.CharField(max_length=8, verbose_name='用户昵称', help_text='只允许8位字符', default='匿名用户')
    pwd = models.CharField(max_length=16, verbose_name='用户的密码', help_text='这是用户密码')
    sex = models.BooleanField(verbose_name='用户性别', help_text='1为男，0为女', default=True)
    sign = models.CharField(max_length=32, verbose_name='用户简短的签名', help_text='字符串', default='')
    poster = models.ImageField(verbose_name='用户的头像', help_text='一个图片路径', upload_to='lsrc', default='')
    add_date = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='每次更新时间', help_text='用来回溯', auto_now=True)
    level = models.BooleanField(verbose_name='用户是否有管理员权限', default=False)


class UserOf(models.Model):
    """
    用户关系表
    """
    uid = models.IntegerField(verbose_name='用户id')
    pid = models.IntegerField(verbose_name='模块id')


class Label(models.Model):
    """
    标签表
    """
    title = models.CharField(max_length=32, verbose_name='标签内容', help_text='如java，python')


class LabelOf(models.Model):
    """
    标签关系表
    """
    # mid = models.IntegerField(verbose_name='所属的模块id')
    pid = models.IntegerField(verbose_name='所属内容id')
    uid = models.IntegerField(verbose_name='标签所属用户id')
    did = models.IntegerField(verbose_name='关联的标签id')


class Picture(models.Model):
    """
    图片表
    """
    title = models.CharField(max_length=16, verbose_name='照片标题')
    src = models.ImageField(verbose_name='照片地址')


class PictureOf(models.Model):
    """
    图片关系表
    """
    pid = models.IntegerField(verbose_name='所属内容id')
    uid = models.IntegerField(verbose_name='所属用户id')
    did = models.IntegerField(verbose_name='关联的图片id')

# Generated by Django 3.2 on 2021-05-08 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='一个新的相册', max_length=32, verbose_name='相册标题')),
                ('detail', models.CharField(default='', max_length=64, verbose_name='这个相册的详细介绍')),
                ('poster', models.IntegerField(verbose_name='相册封面')),
                ('date', models.DateTimeField(default=datetime.timezone, verbose_name='相册创建时间')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='相册更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='一个新文件', max_length=32, verbose_name='文件标题')),
                ('poster', models.IntegerField(verbose_name='该资源封面')),
                ('src', models.FileField(upload_to='File', verbose_name='文件路径')),
                ('date', models.DateTimeField(default=datetime.timezone, verbose_name='文件上传时间')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='一个新的标签', max_length=64, verbose_name='标签')),
                ('date', models.DateTimeField(default=datetime.timezone, verbose_name='标签创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='LabelOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='所属用户')),
                ('pid', models.IntegerField(verbose_name='所属模块')),
                ('type', models.IntegerField(verbose_name='模块类型')),
                ('lid', models.IntegerField(verbose_name='标签')),
            ],
        ),
        migrations.CreateModel(
            name='Learn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.IntegerField(default=0, help_text='父节点为0则是根节点', verbose_name='父节点')),
                ('order', models.IntegerField(default=0, verbose_name='该父节点下的第几位')),
                ('title', models.CharField(default='一个新节点', max_length=32, verbose_name='标题')),
                ('section', models.BooleanField(default=False, verbose_name='该项下是否有文章')),
                ('detail', models.TextField(default='', verbose_name='该项的详细解释')),
                ('date', models.DateTimeField(default=datetime.timezone, verbose_name='创建时间')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='每次更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='一个新的API', max_length=32, verbose_name='我的API，或者我的导航')),
                ('src', models.TextField(verbose_name='API路径')),
                ('date', models.DateTimeField(default=datetime.timezone, verbose_name='创建时间')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='一个新图片', max_length=32, verbose_name='图片标题')),
                ('detail', models.CharField(default='', max_length=64, verbose_name='图片备注')),
                ('date', models.DateTimeField(default=datetime.timezone, verbose_name='图片上传时间')),
                ('src', models.ImageField(upload_to='picture', verbose_name='图片路径')),
            ],
        ),
        migrations.CreateModel(
            name='PictureOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='图片路径')),
                ('pid', models.IntegerField(verbose_name='图片id')),
                ('type', models.IntegerField(verbose_name='所属模组')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='一个新的文章', max_length=32, verbose_name='文章标题')),
                ('detail', models.TextField(default='', verbose_name='文章内容')),
                ('date', models.DateTimeField(default=datetime.timezone, verbose_name='文章创建时间')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='文章更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='SectionOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='所属学习计划')),
                ('pid', models.IntegerField(verbose_name='文章id')),
            ],
        ),
        migrations.CreateModel(
            name='Thinking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='一个新的想法', max_length=32, verbose_name='文章标题')),
                ('detail', models.TextField(default='', verbose_name='文章内容')),
                ('date', models.DateTimeField(default=datetime.timezone, verbose_name='创建时间')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='文章更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(help_text='可以是邮箱', max_length=64, verbose_name='账户id')),
                ('pwd', models.CharField(max_length=64, verbose_name='账户密码')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='匿名用户', max_length=32, verbose_name='账户姓名')),
                ('sex', models.BooleanField(default=True, help_text='false为女，Ture为男', verbose_name='账户性别')),
                ('sign', models.TextField(default='', verbose_name='账户个性前面')),
                ('uid', models.IntegerField(verbose_name='账户id')),
                ('poster', models.IntegerField(default=0, verbose_name='账户头像')),
                ('date', models.DateTimeField(default=datetime.timezone, verbose_name='账户创建时间')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='账户内容更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='UserOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='用户')),
                ('pid', models.IntegerField(verbose_name='所属模块')),
                ('type', models.IntegerField(verbose_name='所属模块')),
            ],
        ),
    ]

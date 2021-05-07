# Generated by Django 3.2 on 2021-05-02 15:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_learn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='所属用户id')),
                ('pid', models.IntegerField(verbose_name='该文章所属资源')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('detail', models.TextField(verbose_name='文本内容')),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建的时间')),
                ('mod_date', models.DateTimeField(auto_now=True, help_text='用来回溯', verbose_name='每次更新时间')),
            ],
        ),
    ]

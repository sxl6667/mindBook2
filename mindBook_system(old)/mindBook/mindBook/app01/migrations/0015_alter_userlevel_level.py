# Generated by Django 3.2 on 2021-05-05 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0014_userlevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlevel',
            name='level',
            field=models.IntegerField(default=0, verbose_name='用户等级'),
        ),
    ]

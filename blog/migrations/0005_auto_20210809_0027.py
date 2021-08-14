# Generated by Django 3.1 on 2021-08-08 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210808_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='name',
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='subject',
            field=models.CharField(max_length=69, null=True),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 9, 0, 27, 47, 79379)),
        ),
    ]
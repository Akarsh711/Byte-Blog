# Generated by Django 3.1 on 2021-04-16 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210416_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 16, 12, 53, 35, 841897)),
        ),
    ]

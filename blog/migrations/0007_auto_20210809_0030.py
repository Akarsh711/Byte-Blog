# Generated by Django 3.1 on 2021-08-08 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210809_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 9, 0, 30, 44, 186208)),
        ),
    ]

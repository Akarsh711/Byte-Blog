# Generated by Django 3.1 on 2021-08-05 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 11, 26, 23, 292821)),
        ),
        migrations.DeleteModel(
            name='UserManage',
        ),
    ]
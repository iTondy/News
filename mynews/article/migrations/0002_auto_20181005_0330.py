# Generated by Django 2.1.1 on 2018-10-05 03:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publishdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 5, 3, 30, 31, 748960), verbose_name='发布日期'),
        ),
    ]

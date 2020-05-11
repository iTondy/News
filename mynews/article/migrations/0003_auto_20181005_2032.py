# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-05 12:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20181005_0330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.RenameField(
            model_name='article',
            old_name='detail',
            new_name='det',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publishdate',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 5, 20, 32, 56, 726282), verbose_name='发布日期'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Tags', verbose_name='标签'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 09:09
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('df_shouye', '0010_auto_20170901_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gcontent',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gintroduce',
            field=tinymce.models.HTMLField(default=b'', null=True),
        ),
    ]

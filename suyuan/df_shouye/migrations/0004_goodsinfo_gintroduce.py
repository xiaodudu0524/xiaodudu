# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 07:14
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('df_shouye', '0003_goodsinfo_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='gintroduce',
            field=tinymce.models.HTMLField(default=b''),
        ),
    ]

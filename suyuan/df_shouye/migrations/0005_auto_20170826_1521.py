# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_shouye', '0004_goodsinfo_gintroduce'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsinfo',
            name='company_address',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='company_president',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]

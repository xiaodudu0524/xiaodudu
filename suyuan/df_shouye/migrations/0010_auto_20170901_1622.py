# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 08:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_shouye', '0009_auto_20170901_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fertilizer',
            name='isDelete',
        ),
        migrations.RemoveField(
            model_name='growimage',
            name='isDelete',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0002_userinfo_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
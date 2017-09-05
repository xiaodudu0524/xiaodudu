# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('df_shouye', '0011_auto_20170901_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pesticide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useTime', models.DateTimeField()),
                ('pesticidename', models.CharField(max_length=50)),
                ('yongLiang', models.CharField(max_length=50)),
                ('pingPai', models.CharField(max_length=50)),
                ('gongYingshang', models.CharField(max_length=50)),
                ('pType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_shouye.GoodsInfo')),
            ],
        ),
    ]
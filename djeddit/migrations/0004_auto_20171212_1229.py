# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-12 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djeddit', '0003_auto_20170616_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='user_agent',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-11 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
    ]
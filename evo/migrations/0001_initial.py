# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-08 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('type1', models.CharField(max_length=200)),
                ('type2', models.CharField(max_length=200)),
                ('total', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('spatk', models.IntegerField()),
                ('spdef', models.IntegerField()),
                ('speed', models.IntegerField()),
            ],
        ),
    ]

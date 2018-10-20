# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-14 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hkname', models.CharField(max_length=10)),
                ('hkpwd', models.CharField(max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='blogtxt',
            fields=[
                ('blogid', models.AutoField(primary_key=True, serialize=False)),
                ('blogtitle', models.CharField(max_length=20)),
                ('blogcontenta', models.CharField(max_length=255)),
                ('blogcontentb', models.CharField(max_length=255)),
                ('blogcontentc', models.CharField(max_length=255)),
                ('bloghref', models.CharField(max_length=255)),
                ('blogimg', models.CharField(max_length=255, null=True)),
                ('blogtime', models.CharField(max_length=20)),
                ('blogread', models.IntegerField()),
                ('blogreview', models.IntegerField()),
                ('blogzan', models.IntegerField()),
                ('bloglow', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('blogid', models.AutoField(primary_key=True, serialize=False)),
                ('bloggre', models.CharField(max_length=255)),
                ('blogtype', models.CharField(max_length=5)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-02-21 00:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='\u043f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442')),
                ('title', models.CharField(max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('title_eng', models.CharField(max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435(\u0430\u043d\u0433\u043b.)')),
                ('title_tr', models.CharField(max_length=50, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435(\u0442\u0443\u0440\u0435\u0446.)')),
                ('img', models.ImageField(upload_to=post.models.image_upload_to, verbose_name='\u0418\u043a\u043e\u043d\u043a\u0430')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=post.models.image_upload_to, verbose_name='\u0418\u043a\u043e\u043d\u043a\u0430')),
                ('title', models.CharField(max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('title_eng', models.CharField(max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435(\u0430\u043d\u0433\u043b.)')),
                ('title_tr', models.CharField(max_length=50, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435(\u0442\u0443\u0440\u0435\u0446.)')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('description_eng', models.CharField(max_length=500, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435(\u0430\u043d\u0433\u043b.)')),
                ('description_tr', models.CharField(max_length=500, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435(\u0442\u0443\u0440\u0435\u0446.)')),
                ('weight', models.CharField(max_length=100, null=True, verbose_name='\u0412\u0435\u0441(\u0412\u044b\u0445\u043e\u0434)')),
                ('price', models.IntegerField(null=True, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Category', verbose_name='\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u043d\u044e',
                'verbose_name_plural': '\u041c\u0435\u043d\u044e',
            },
        ),
    ]

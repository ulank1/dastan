# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-03-03 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20180301_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='position',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u043f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title_eng',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435(\u0430\u043d\u0433\u043b.)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title_kg',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435(\u043a\u044b\u0440\u0433.)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title_tr',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435(\u0442\u0443\u0440\u0435\u0446.)'),
        ),
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='food',
            name='description_eng',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435(\u0430\u043d\u0433\u043b.)'),
        ),
        migrations.AlterField(
            model_name='food',
            name='description_kg',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435(\u043a\u044b\u0440\u0433.)'),
        ),
        migrations.AlterField(
            model_name='food',
            name='description_tr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435(\u0442\u0443\u0440\u0435\u0446.)'),
        ),
        migrations.AlterField(
            model_name='food',
            name='dish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Category', verbose_name='\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='food',
            name='title_eng',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435(\u0430\u043d\u0433\u043b.)'),
        ),
        migrations.AlterField(
            model_name='food',
            name='title_kg',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435(\u043a\u044b\u0440\u0433.)'),
        ),
        migrations.AlterField(
            model_name='food',
            name='title_tr',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435(\u0442\u0443\u0440\u0435\u0446.)'),
        ),
        migrations.AlterField(
            model_name='food',
            name='weight',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0412\u0435\u0441(\u0412\u044b\u0445\u043e\u0434)'),
        ),
    ]

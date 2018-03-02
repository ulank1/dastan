# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

def image_upload_to(instance, filename):
    return "images/%s" % filename


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    position = models.IntegerField(verbose_name="приоритет")
    title = models.CharField(max_length=50, verbose_name="Название")
    title_eng = models.CharField(max_length=50, verbose_name="Название(англ.)")
    title_tr = models.CharField(max_length=50, verbose_name="Название(турец.)",null=True)
    title_kg = models.CharField(max_length=50, verbose_name="Название(кырг.)",null=True)
    img = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.title


class Food(models.Model):
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    dish = models.ForeignKey(Category, verbose_name='категория', null=True)
    img = models.ImageField(upload_to=image_upload_to, verbose_name='Иконка')
    title = models.CharField(max_length=50, verbose_name="Название")
    title_eng = models.CharField(max_length=50, verbose_name="Название(англ.)")
    title_tr = models.CharField(max_length=50, verbose_name="Название(турец.)", null=True)
    title_kg = models.CharField(max_length=50, verbose_name="Название(кырг.)",null=True)
    description = models.CharField(max_length=500, verbose_name="Описание", null=True)
    description_eng = models.CharField(max_length=500, verbose_name="Описание(англ.)", null=True)
    description_tr = models.CharField(max_length=500, verbose_name="Описание(турец.)", null=True)
    description_kg = models.CharField(max_length=500, verbose_name="Описание(кырг.)", null=True)
    weight = models.CharField(max_length=100, verbose_name="Вес(Выход)", null=True)
    price = models.IntegerField(verbose_name="Стоимость", null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.title

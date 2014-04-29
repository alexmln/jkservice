#-*-coding:utf-8-*-
from django.db import models


class NewsModel(models.Model):
    brief = models.TextField('Краткое содержание:', blank=False)
    news_date = models.DateTimeField('Дата публикации:')
    news_text = models.TextField('Текст новости:', blank=False)

    class Meta():
        verbose_name_plural = 'Новости'

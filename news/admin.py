from django.contrib import admin
from news.models import NewsModel


class NewsAdmin(admin.ModelAdmin):
    list_display = ('brief', 'news_date')

admin.site.register(NewsModel, NewsAdmin)
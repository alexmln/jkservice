from django.shortcuts import render
from news.models import NewsModel


def index(request):
    news_list = NewsModel.objects.all().order_by('-news_date')[:10]
    return render(request, 'news/index.html', {'news': news_list })
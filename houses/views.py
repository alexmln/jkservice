from django.shortcuts import render
from houses.models import House


def index(request):
    houses = House.objects.all().order_by('settlement')
    return render(request, 'houses/index.html', {'houses': houses })


def detail(request, house_id):
    return render(request, 'houses/detail.html')
from django.shortcuts import render
from houses.models import House


def index(request):
    houses = House.objects.all().order_by('-settlement', 'house_number')
    return render(request, 'houses/index.html', {'houses': houses })


def detail(request, house_id):
    house = House.objects.get(pk=house_id)
    return render(request, 'houses/detail.html', {'house': house })
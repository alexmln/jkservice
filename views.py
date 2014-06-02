#-*-coding:utf-8-*-
import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db import connection
from forms import WaterForm
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from news.models import NewsModel


def index(request):
    news_list = NewsModel.objects.values('id', 'news_date', 'brief').order_by('-news_date')[:5]
    return render(request, 'jkservice/index.html', {'news': news_list})


def watermet(request):
    rightnow = datetime.date.today()
    if rightnow.day < 1:
        return render(request, 'jkservice/cap.html')
    form = WaterForm()
    return render(request, 'jkservice/watermet.html', {'form': form, })


def add_statement(request):
    if request.is_ajax():
        form = WaterForm(request.POST)
        to_json = {}
        if form.is_valid():
            try:
                company = int(request.POST['company'])
                pa = int(request.POST['pa'])
                cwm_1 = request.POST['cwm_1']
                cwm_2 = request.POST['cwm_2']
                hwm_1 = request.POST['hwm_1']
                hwm_2 = request.POST['hwm_2']
                cursor = connection.cursor()
                cursor.execute("""SELECT pa FROM company_%s WHERE pa = %s;""", (company, pa, ))
                if cursor.fetchone() is not None:
                    cursor.execute("""UPDATE company_%s SET cwm_1 = %s, cwm_2 = %s, hwm_1 = %s, hwm_2 = %s, update_time = %s WHERE pa = %s;""", (company, cwm_1, cwm_2, hwm_1, hwm_2, datetime.datetime.now(), pa))
                    to_json['status'] = True
                    to_json['message'] = 'Показания приняты, спасибо.'
                else:
                    to_json['status'] = False
                    to_json['message'] = 'Пожалуйста, проверьте правильность введенных данных и отправьте форму еще раз.'
            except (RuntimeError, TypeError, NameError):
                to_json['status'] = False
                to_json['message'] = 'Ошибка сервера, повторите запрос позднее'
        else:
            to_json['status'] = False
            to_json['message'] = 'Пожалуйста, проверьте правильность введенных данных и отправьте форму еще раз'
        return HttpResponse(json.dumps(to_json), content_type='application/json')
    else:
        raise Http404


def captcha_refresh(request):
    to_json = {}
    if request.is_ajax():
        to_json['key'] = CaptchaStore.generate_key()
        to_json['image'] = captcha_image_url(to_json['key'])
        return HttpResponse(json.dumps(to_json), content_type='application/json')
    else:
        raise Http404
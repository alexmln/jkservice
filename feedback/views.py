#-*-coding:utf-8-*-
import smtplib
import json
from django.http import Http404, HttpResponse
from django.shortcuts import render
from feedback.models import FeedbackForm
from django.core.mail import send_mail, BadHeaderError

def index(request):
    form = FeedbackForm()
    return render(request, 'feedback/index.html', {'form': form})


def send_message(request):
    if request.is_ajax():
        to_json = {}
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            subject = request.POST['subject']
            email = request.POST['email']
            message = u'От: ' + str(email) + u'\nСообщение: ' + request.POST['message']
            try:
                send_mail(subject, message, email, ['fromlnkv@yandex.ru'], fail_silently=False)
                to_json['status'] = True
                to_json['message'] = 'Спасибо, ваше сообщение отправлено.'
            except (smtplib.SMTPException, BadHeaderError):
                to_json['status'] = False
                to_json['message'] = 'Не удалось отправить сообщение, повторите позднее.'
        else:
            to_json['status'] = False
            to_json['message'] = 'Пожалуйста, проверьте правильность введенных данных и отправьте форму еще раз. Обязательно укажите обратный email.'
        return HttpResponse(json.dumps(to_json), content_type='application/json')
    else:
        raise Http404

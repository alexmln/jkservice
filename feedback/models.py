#-*-coding:utf-8-*-
from django.db import models
from django.forms import ModelForm, TextInput, Textarea
from captcha.fields import CaptchaField, CaptchaTextInput


class Feedback(models.Model):
    email = models.EmailField('Ваш email: ')
    subject = models.TextField('Тема: ', blank=True)
    message = models.TextField('Сообщение: ')
    date = models.DateTimeField(auto_now=True)


class FeedbackForm(ModelForm):
    captcha = CaptchaField()
    captcha = CaptchaField(widget=CaptchaTextInput({'class': 'form-control'}))
    class Meta:
        model = Feedback
        fields = ['email', 'subject', 'message']
        widgets = {
            'email': TextInput(attrs={'type': 'email', 'class': 'form-control', 'id': 'email', 'rows': 1, 'cols': 15}),
            'subject': TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'subject', 'rows': 1, 'cols': 15}),
            'message': Textarea(attrs={'class': 'form-control', 'id': 'message', 'rows': 5, 'cols': 20}),
        }

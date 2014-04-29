#-*-coding:utf-8-*-
from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput


class WaterForm(forms.Form):
    choices = (('1', 'УК "Жилкомсервис"',), ('2', 'ТСЖ "Дубровское"',), ('3', 'ТСЖ "Фетинино"',))
    company = forms.ChoiceField(widget=forms.RadioSelect, choices=choices, label='Организация:')
    pa = forms.IntegerField(widget=forms.NumberInput(attrs={'maxlength': '14', 'class': 'form-control'}), label='Лицевой счет:')
    cwm_1 = forms.DecimalField(widget=forms.NumberInput(attrs={'maxlength': '14', 'class': 'form-control'}), label='Счетчик холодной воды 1:')
    cwm_2 = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'maxlength': '14', 'class': 'form-control'}), label='Счетчик холодной воды 2:')
    hwm_1 = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'maxlength': '14', 'class': 'form-control'}), label='Счетчик горячей воды 1:')
    hwm_2 = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'maxlength': '14', 'class': 'form-control'}), label='Счетчик горячей воды 2:')
    captcha = CaptchaField(widget=CaptchaTextInput({'class': 'form-control'}))

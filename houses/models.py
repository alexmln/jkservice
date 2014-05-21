#-*-coding:utf-8-*-
from django.db import models


class House(models.Model):
    SETTLEMENT_CHOICES = (
        ('SE', 'Семенково'),
        ('S2', 'Семенково - 2'),
        ('FO', 'Фофанцево'),
        ('FE', 'Фетинино'),
        ('DO', 'Дорожный'),
        ('AE', 'Аэропорт'),
        ('CU', 'Кувшиново'),
        ('DU', 'Дубровское'),
        ('VO', 'Вологда'),
    )
    STATUS = (
        ('OK', 'Исправный'),
        ('NO', 'Аварийный'),
    )
    house_id = models.AutoField(primary_key=True)
    settlement = models.CharField('Поселение/Город', max_length=2, choices=SETTLEMENT_CHOICES, blank=False)
    street_name = models.CharField('Улица', max_length=30, blank=True)
    house_number = models.CharField('Номер дома', max_length=8, blank=False)
    house_litera = models.CharField('Буква дома', max_length=2, blank=True)
    house_corp = models.CharField('Корпус дома', max_length=2, blank=True)
    house_area = models.CharField('Площадь дома', max_length=10)
    house_year = models.CharField('Год ввода в эксплуатацию', max_length=4)
    house_status = models.CharField('Состояние дома', max_length=2, choices=STATUS, blank=False)
    house_population = models.CharField('Жильцов', max_length=5)
    contract = models.BooleanField('Договор действующий?', default=True)
    comment = models.CharField('Комментарий', max_length=300, blank=True)

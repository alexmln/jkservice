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

    def __unicode__(self):
        if self.house_corp:
            slash = '/'
        else:
            slash = ''
        return self.get_settlement_display() + ' ' + self.street_name + ' ' + str(self.house_number) + slash + str(self.house_corp) + self.house_litera


class Link(models.Model):

    def file(self, filename):
        url = '%s/%s' % (self.house.house_id, filename)
        return url

    CATEGORY_CHOICES = (
        ('DU', 'Договор управления'),
        ('VR', 'Выполняемые работы'),
        ('VO', 'Выполнение обязательств'),
        ('SU', 'Стоиомсть услуг'),
    )
    house = models.ForeignKey(House)
    category = models.CharField('Категория', max_length=2, choices=CATEGORY_CHOICES)
    filename = models.CharField('Имя файла', max_length=100, blank=False)
    upload_file = models.FileField('Файл', upload_to=file)

    def __unicode__(self):
        return self.upload_file.path


class Damage(models.Model):

    house = models.ForeignKey(House)
    general_damage = models.CharField('Общая степень износа', max_length=3, blank=True)
    foundation_damage = models.CharField('Износ фундамента', max_length=3, blank=True)
    walls_damage = models.CharField('Износ несущих стен', max_length=3, blank=True)
    overlap_damage = models.CharField('Износ перекрытий', max_length=3, blank=True)


class Rso(models.Model):

    house = models.ForeignKey(House)
    heating = models.CharField('Поставщик отопления', max_length=20, blank=True)
    heating_uo = models.BooleanField('поставляется через уо', default=False)
    electric = models.CharField('Поставщик электроэнергии', max_length=20, blank=True)
    electric_uo = models.BooleanField('поставляется через уо', default=False)
    gas = models.CharField('Поставщик газа', max_length=20, blank=True)
    gas_uo = models.BooleanField('поставляется через уо', default=False)
    hot_water = models.CharField('Поставщик горячей воды', max_length=20, blank=True)
    hot_water_uo = models.BooleanField('поставляется через уо', default=False)
    cold_water = models.CharField('Поставщик холодной воды', max_length=20, blank=True)
    cold_water_uo = models.BooleanField('поставляется через уо', default=False)
    wastewater = models.CharField('Поставщик водоотведения', max_length=20, blank=True)
    wastewater_uo = models.BooleanField('поставляется через уо', default=False)
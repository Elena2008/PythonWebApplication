from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

CITY = (
    (1, 'Voronezh'),
    (2, 'Moscow'),
    (3, 'St. Petersburg'),
    (4, 'Novgorod')
)


#  пользователь сайта
class Person(AbstractUser):
    ID = models.DecimalField(primary_key=True, max_length=100)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.TextField(max_length=1, blank=True, choices=CITY, help_text='Выберите город')
    mobile_phone = models.TextField(max_length=11,blank=True)
    isEmployer = models.BooleanField(default=False)


#  отклик
class Response:
    vacancy = models.ForeignKey('Job', on_delete=models.SET_NULL, null=False)
    employee = models.ForeignKey('Person', on_delete=models.SET_NULL, null=False)
    date_of_response = models.DateTimeField()
    commentary = models.TextField(max_length=300,blank=True)


#  предложение о работе
class Job(models.Model):
    CATEGORY = (
        (1, 'Programmer'),
        (2, 'Medicine'),
        (3, 'OfficeManager'),
        (4, 'Military')
    )

    GRAPHIC = (
        (1, 'FullDay'),
        (2, 'PartDay')
    )

    category = models.TextField(max_length=1, blank=True, choices=CATEGORY, default=1, help_text='Выберите категорию')
    wage = models.DecimalField(max_length=10)
    graphic = models.TextField(max_length=1, blank=True, choices=GRAPHIC, help_text='Выберите график работы')
    employer = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    dateOfPlacement = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-dateOfPlacement"]


# бан между работником и работодателем
class Ban:
    employee = models.ForeignKey('Person', on_delete=models.SET_NULL, null=False)
    employer = models.ForeignKey('Person', on_delete=models.SET_NULL, null=False)
    date_of_ban = models.DateTimeField()
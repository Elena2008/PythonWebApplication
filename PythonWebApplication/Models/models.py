from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


#  пользователь сайта
class Person(AbstractUser):
    CITY = (
        (1, 'Voronezh'),
        (2, 'Moscow'),
        (3, 'St. Petersburg'),
        (4, 'Novgorod')
    )

    #  ID = models.DecimalField(primary_key=True, max_length=100, decimal_places=0, max_digits=10)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.IntegerField(blank=True, choices=CITY, help_text='Выберите город', default=1)
    mobile_phone = models.TextField(max_length=11,blank=True)
    isEmployer = models.BooleanField(default=False)

    def __str__(self):
        return self.username.__str__()


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

    category = models.IntegerField(blank=True, choices=CATEGORY, default=1, help_text='Выберите категорию')
    wage = models.DecimalField(max_length=10, decimal_places=2, max_digits=10)
    graphic = models.IntegerField(blank=True, choices=GRAPHIC, help_text='Выберите график работы',default=1)
    employer = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True,limit_choices_to={'isEmployer': True})
    date_of_placement = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.category.__str__() +' '+ self.wage.__str__() + ' ' + self.employer.__str__()

    class Meta:
        ordering = ["-date_of_placement"]


#  отклик
class Response(models.Model):
    vacancy = models.ForeignKey('Job', on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    date_of_response = models.DateTimeField()
    commentary = models.TextField(max_length=300,blank=True)

    def __str__(self):
        return self.vacancy.__str__() + self.employee.__str__()

    class Meta:
        ordering = ["-date_of_response"]


# бан между работником и работодателем
class Ban(models.Model):
    employee = models.ForeignKey(Person, related_name='employee', on_delete=models.SET_NULL, null=True)
    employer = models.ForeignKey(Person, related_name='employer', on_delete=models.SET_NULL, null=True)
    date_of_ban = models.DateTimeField()

    def __str__(self):
        return self.employee.__str__() + ' ' + self.employer.__str__()

    class Meta:
        ordering = ["-date_of_ban"]

# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django import forms


class PersonCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Person
        fields = ('username', 'email', 'city', 'mobile_phone', 'isEmployer')


class PersonChangeForm(UserChangeForm):

    class Meta:
        model = Person
        fields = ('username', 'email', 'city', 'mobile_phone', 'isEmployer')


class JobCreationForm(forms.Form):

    class Meta(forms.Form):
        model = Job
        fields = ('category', 'graphic', 'wage', 'employer', 'date_of_placement')

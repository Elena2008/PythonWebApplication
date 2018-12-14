# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Slave


class SlaveCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Slave
        fields = ('username', 'email')


class SlaveChangeForm(UserChangeForm):

    class Meta:
        model = Slave
        fields = ('username', 'email')
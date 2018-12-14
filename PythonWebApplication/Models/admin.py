from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import SlaveCreationForm, SlaveChangeForm
from .models import Slave
# Register your models here.


class SlaveAdmin(UserAdmin):
    add_form = SlaveCreationForm
    form = SlaveChangeForm
    model = Slave
    list_display = ['email', 'username',]


admin.site.register(Slave, SlaveAdmin)
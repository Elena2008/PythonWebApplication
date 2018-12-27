from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import PersonCreationForm, PersonChangeForm
from .models import *
# Register your models here.


class PersonAdmin(UserAdmin):
    add_form = PersonCreationForm
    form = PersonChangeForm
    model = Person
    list_display = ['email', 'username', ]


admin.site.register(Person, PersonAdmin)
admin.site.register(Job)
admin.site.register(Ban)
admin.site.register(Response)


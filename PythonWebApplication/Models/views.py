from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from .forms import PersonCreationForm

class SignUp(generic.CreateView):
    form_class = PersonCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
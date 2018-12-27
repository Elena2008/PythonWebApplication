from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import *


class SignUp(generic.CreateView):
    form_class = PersonCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class Home(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            if user.isEmployer:
                context['items'] = Response.objects.filter(vacancy__in=Job.objects.filter(employer=user))
            else:
                context['items'] = Job.objects.exclude(employer__in=Ban.objects.filter(employee=user).values('employer'))
        return context


class AddVacancy(generic.CreateView):
    form_class = JobCreationForm
    success_url = reverse_lazy('vacancy')
    template_name = 'vacancy.html'



from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('vacancy/', views.AddVacancy.as_view(), name='vacancy'),
    path('home/', views.Home.as_view(template_name='home.html'), name='home'),

]
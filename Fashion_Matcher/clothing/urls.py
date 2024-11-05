from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('male/', views.male, name='male'),
    path('female/', views.female, name='female'),
]

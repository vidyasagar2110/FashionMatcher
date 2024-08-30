from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('male/', views.male_preferences, name='male_preferences'),
    path('female/', views.female_preferences, name='female_preferences'),
]

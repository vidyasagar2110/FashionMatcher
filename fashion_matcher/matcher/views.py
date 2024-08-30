from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def male_preferences(request):
    # Add logic for male preferences page
    return render(request, 'male_preferences.html')

def female_preferences(request):
    # Add logic for female preferences page
    return render(request, 'female_preferences.html')

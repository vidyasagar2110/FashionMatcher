from django.shortcuts import render

def home(request):
    return render(request, 'clothing/home.html')

def male(request):
    return render(request, 'clothing/male.html')

def female(request):
    return render(request, 'clothing/female.html')

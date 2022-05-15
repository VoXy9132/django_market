from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def shop(request):
    return render(request, 'first_app/shop.html')

def support(request):
    return render(request, 'first_app/support.html')

def logout(request):
    return render(request, 'first_app/logout.html')

def developers(request):
    return render(request, 'first_app/developers.html')




from django.shortcuts import render
from .models import Vehicle

# Create your views here.

def main(request):
    return render(request, 'main.html')

def vehicles(request):

    cars=Vehicle.objects.all()


    return render(request, 'vehicles.html', {'cars': cars})

def payment(request):
    return render(request, 'payment.html')

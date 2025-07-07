from django.shortcuts import render
from home.models import *

# Create your views here.

def index(request):
    return render(request, 'admin.html')

def customers(request):
   
    customers = Customer.objects.all()
    return render(request, 'customers.html', context={'customers':customers})

def create_customer(request):
    return render(request, 'create_customer.html')



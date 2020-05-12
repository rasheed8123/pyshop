from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def rash(request):
    products = Product.objects.all()
    return render(request,'rash.html',{'products': products})

def ahm(request):
    return HttpResponse('new prep')
# Create your views here.

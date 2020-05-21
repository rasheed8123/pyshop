from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .import templates

def plan(request):
    return render(request,'plan.html')


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')


def career(request):
    return render(request,'career.html')



def haappylt(request):
    return render(request,'haappylt.html')




def haappy(request):
    return render(request,'haappy.html')

# Create your views here.

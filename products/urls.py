from django.urls import path
from . import views

urlpatterns = [
    path('',views.rash),
    path('ahm',views.ahm),
]
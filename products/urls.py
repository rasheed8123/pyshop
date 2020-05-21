from django.urls import path
from . import views
from . import templates


urlpatterns = [
    path('',views.haappy),
    path('products/templates/contact',views.contact),
    path('products/templates/plan',views.plan),
    path('products/templates/about',views.about),
    path('products/templates/career',views.career),
    path('products/templates/haappy',views.haappylt),

]
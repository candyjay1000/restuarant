from django.contrib import admin
from django.urls import path
from order.models import Order
from .views import *

urlpatterns = [
    path('order',order,name='order'),
  
    
]

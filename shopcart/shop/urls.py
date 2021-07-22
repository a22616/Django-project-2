from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='shopHome'),
    path('productview/<int:myid>',views.productview,name='productview'),
    
]
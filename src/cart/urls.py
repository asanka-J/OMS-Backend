from django.contrib import admin
from django.urls import path , include
from .views import (updateItem)

urlpatterns = [
    path('update/',updateItem, name='cart-update'),


]

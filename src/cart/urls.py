from django.contrib import admin
from django.urls import path , include
from .views import (updateItem ,checkout ,cart ,order_history ,order_sucess)

urlpatterns = [
    path('',cart, name='cart-cart'),
    path('checkout/',checkout, name='cart-checkout'),
    path('history/',order_history, name='cart-history'),
    path('sucess/',order_sucess, name='cart-history'),


   
    path('update/',updateItem, name='cart-update'),
    




]

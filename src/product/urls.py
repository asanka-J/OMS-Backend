from django.contrib import admin
from django.urls import path , include
from .views import ( categoryList, productDetail, shopList, shopProductList, shopProduct)

urlpatterns = [
    path('', categoryList, kwargs=None, name='category-list'),
    # path('<slug:category>', shopList, kwargs=None, name='shop-list'),
    # path('<slug:category>/<slug:shop>/', shopProductList, kwargs=None, name='product-list'),
    # path('<slug:shop>/<slug:product>/', shopProduct, kwargs=None, name='product-detail'),
    path('product/', shopProduct, kwargs=None, name='product-detail'),



]

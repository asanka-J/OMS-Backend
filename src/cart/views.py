from django.shortcuts import render
from django.http import JsonResponse
import json

from src.product.models import Product
from src.order.models import Order , OrderItem
from .utils import cartData


def updateItem(request):
    data = json.loads(request.body)

    product_id = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
   
    
    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('Item was added', safe=False)



def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	total = data['total']


	context = {'items':items, 'order':order, 'cartItems':cartItems,'total':total}
	return render(request, 'frontend/checkout/cart.html',context)

def checkout(request):
    return render(request, 'frontend/checkout/checkout.html')

def order_history(request):
    return render(request, 'frontend/checkout/order_history.html')

def order_sucess(request):
    return render(request, 'frontend/checkout/order_success.html')
    
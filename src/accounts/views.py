from django.shortcuts import render
from django.contrib.auth import logout
from src.product.models import Product

def index(request):
    return render(request, 'frontend/index.html')
   
def test(request):
    products = Product.objects.all() 
    
    context={'products':products}
    return render(request, 'test.html', context)

def not_available(request):
    return render(request, 'frontend/404.html')

def about(request):
    return render(request, 'frontend/about.html')

def faq(request):
    return render(request, 'frontend/faq.html')    

def register(request):
    return render(request, 'accounts/register.html')    

def login(request):
    return render(request, 'accounts/login.html')  

def forgot_password(request):
    return render(request, 'accounts/forget_pwd.html')  

# customer dashboard
def customer_dashboard(request):
    return render(request, 'frontend/dashboard/dashboard.html') 

def comming_soon(request):
    return render(request, 'frontend/comming_soon.html')   

def logout(request):
    logout(request)
   
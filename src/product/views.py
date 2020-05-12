from django.shortcuts import render

   
def categoryList(request):
    return render(request, 'frontend/category_page.html')

def productDetail(request):
    return render(request, 'frontend/product_detail.html')

def shopList(request):
    return render(request, 'frontend/category_page.html')

def shopProductList(request):
    return render(request, 'frontend/category_page.html')

def shopProduct(request):
    return render(request, 'frontend/product_detail2.html')


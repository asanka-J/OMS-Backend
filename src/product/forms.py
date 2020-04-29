from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .models import Product, Category , Product_Images

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class ProductImagesForm(ModelForm):

    class Meta:
        model = Product_Images
        fields = '__all__'

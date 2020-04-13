from django.contrib.auth import get_user_model
from graphene_django.forms.mutation import DjangoModelFormMutation
from ...product.forms import ProductForm, CategoryForm , ProductImagesForm

import graphene
from graphene_django import DjangoObjectType
from ...product.models import Product_Images, Product, Category

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class ProductImageType(DjangoObjectType):
    class Meta:
        model = Product_Images

class CreateProductFMutation(DjangoModelFormMutation):
    product = graphene.Field(ProductType)
    class Meta:
        form_class = ProductForm
       
class CreatCategoryFMutation(DjangoModelFormMutation):
    category = graphene.Field(CategoryType)
    class Meta:
        form_class = CategoryForm

class CreatProductImageFMutation(DjangoModelFormMutation):
    productImageType = graphene.Field(ProductImageType)
    class Meta:
        form_class = ProductImagesForm


class Query(graphene.ObjectType):
    product = graphene.List(ProductType)
    category = graphene.List(CategoryType) 
    productImages = graphene.List(ProductImageType)
    Parentcategory = graphene.Field(CategoryType) 

    def resolve_product(self, info):
        return Product.objects.all()

    def resolve_category(self, info):
        return Category.objects.objects.all()

    def resolve_productImages(self, info, email):
        return get_user_model().objects.all()
    
    def resolve_Parentcategory(self, info):
        return get_user_model().objects.filter(parent=None).all()


class Mutation(graphene.ObjectType):

    createProduct = CreateProductFMutation.Field()
    createProductImage = CreatProductImageFMutation.Field()
    createCategory = CreatCategoryFMutation.Field()

from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.utils.translation import gettext as _
from .managers import ParentCategoryManager
from django.db.models.signals import pre_save
from .signals import slug_generator

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True)
    background_image = VersatileImageField(upload_to="category-backgrounds", blank=True, null=True)
    background_image_alt = models.CharField(max_length=128, blank=True)
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET("parent-deleted"))

    # parent_objects = ParentCategoryManager()

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    sku =  models.CharField(max_length=55, blank=True, null=True)
    category = models.ManyToManyField(Category)
    brand = models.TextField(blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    sale_price = models.TextField(blank=True, null=True)
    fetured = models.IntegerField(blank=True, null=True)
    available = models.BooleanField(default=True)
    
    
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.name


class Product_Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='images')
    product_image = VersatileImageField(upload_to="Product-Images", blank=True, null=True)

    def __str__(self):
         return self.product.name


pre_save.connect(slug_generator, sender=Category)
pre_save.connect(slug_generator, sender=Product)
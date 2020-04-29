from django.db import models
from src.accounts.models import User
from src.product.models import Product

class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    products    = models.ManyToManyField(Product, blank=True)
    subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)


    def __str__(self):
        return str(self.id)
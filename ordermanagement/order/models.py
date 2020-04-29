from django.db import models
from ordermanagement.product.models import Product
from ordermanagement.accounts.models import User,Address
from ordermanagement.cart.models import Cart


class Order(models.Model):
    
    order_items = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True )
    is_paid = models.BooleanField(default=False)
    shipping_address    = models.ForeignKey(Address, related_name="shipping_address",null=True, blank=True, on_delete=models.SET_NULL)
    billing_address     = models.ForeignKey(Address, related_name="billing_address", null=True, blank=True,on_delete=models.SET_NULL)
    shipping_cost = models.IntegerField(blank=True, null=True, default=0)
    # customer = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.customer.name




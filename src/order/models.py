from django.db import models
from src.product.models import Product
from src.accounts.models import User,Address
from src.cart.models import Cart


class Order(models.Model):
    
    customer = models.ForeignKey(User,on_delete=models.SET_NULL , blank=True , null = True)
    is_paid = models.BooleanField(default=False)
    shipping_address    = models.ForeignKey(Address, related_name="shipping_address",null=True, blank=True, on_delete=models.SET_NULL)
    billing_address     = models.ForeignKey(Address, related_name="billing_address", null=True, blank=True,on_delete=models.SET_NULL)
    shipping_cost = models.IntegerField(blank=True, null=True, default=0)
    transaction_id = models.CharField(max_length=256, blank=True)
    complete = models.BooleanField(default=False)
   
    def __str__(self): 
        return self.customer.first_name + str(self.id)
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        count = sum([item.quantity for item in orderitems])
        return count   

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity*float(item.product.sale_price) for item in orderitems])
        return total 



class OrderItem(models.Model):
    
    product = models.ForeignKey(Product,on_delete=models.SET_NULL , blank=True , null = True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL , blank=True , null = True)
    quantity = models.IntegerField(blank=True, null=True, default=0)
    
    def __str__(self): 
        return  self.product.name + str(self.order.id)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total



from django.db import models
from ordermanagement.catalogue.models import product
from ordermanagement.customer.models import Customer


class Order(models.Model):
    name = models.CharField(max_length=100)
    total = models.TextField()
    product = models.ManyToManyField(product)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


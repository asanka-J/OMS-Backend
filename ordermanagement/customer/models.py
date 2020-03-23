from django.db import models
from ordermanagement.catalogue.models import product

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone1 = models.TextField(null=True)
    phone2 = models.TextField(null=True)

    

    def __str__(self):
        return self.name


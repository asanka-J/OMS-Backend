from django.db import models


class product(models.Model):
    name = models.CharField(max_length=100)
    cost = models.TextField()
    selling = models.TextField()
    
   
    def __str__(self):
        return self.name

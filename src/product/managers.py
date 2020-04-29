from django.db import models

class ProudctManager(models.Manager):
    pass


class ParentCategoryManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter(parent=None)
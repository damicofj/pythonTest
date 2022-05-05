from locale import currency
from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    language = models.CharField(max_length=30)
    currency = models.CharField(max_length=30)
    
    # we add this so it returns the name in the admin page, instead of just 'object x'
    def __str__(self):
        return self.name

    
# JSONField


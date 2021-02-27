from django.db import models
from opna.models import Categories
# Create your models here.

class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subscription = models.CharField(max_length=50, choices = Categories.choices, default = Categories.ENGLISH)
    
    def __str__ (self):
        return self.name + ' ' + self.surname + '-' + self.subscription
    
    
from django.db import models 
from opla.models import Levels
# Create your models here.


class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # subscription = models.CharField(max_length=50, choices = Categories.choices, default = Categories.ENGLISH)
    subscriptionLevel = models.CharField(max_length=50, choices = Levels.choices, default = Levels.A1)
    slug = models.SlugField(blank=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return self.name + ' ' + self.surname + '-' + self.subscription
    
    @property
    def subscriber_count(self):
        return self.email_set.all().count()
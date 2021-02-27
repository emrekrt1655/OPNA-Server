from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Categories(models.TextChoices):
    ENGLISH = 'english',
    GERMAN = 'german',
    TURKISH = 'turkish',
    FRENCH = 'french',
    RUSSIAN = 'russian',
    UKRAINIAN = 'ukranian',
    SPANISH = 'spanish',
    ARABIC = 'arabic',
    ROMANIAN = 'romanian',
    CHINESE = 'chinese'
    
class News(models.Model):
    headtitle = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    category = models.CharField(max_length=50, choices = Categories.choices, default = Categories.ENGLISH)
    image = models.CharField(max_length=1000, default= "https://images.pexels.com/photos/97050/pexels-photo-97050.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940")
    excerpt = models.CharField(max_length=300, blank=True)
    published =models.BooleanField(default=False)
    day = models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    date_created = models.DateTimeField(auto_now_add=True)
    newstitle_one = models.CharField(max_length=300)
    news_one_content = models.TextField()
    newstitle_two = models.CharField(max_length=300)
    news_two_content = models.TextField()
    newstitle_three = models.CharField(max_length=300, blank=True)
    news_three_content = models.TextField(blank=True)
    newstitle_four = models.CharField(max_length=300, blank=True)
    news_four_content = models.TextField(blank=True)
    newstitle_five = models.CharField(max_length=300, blank=True)
    news_five_content = models.TextField(blank=True)
    vocab_one = models.CharField(max_length=200)
    vocab_one_mean = models.TextField()
    vocab_two = models.CharField(max_length=200)
    vocab_two_mean = models.TextField()
    vocab_three = models.CharField(max_length=200)
    vocab_three_mean = models.TextField()
    vocab_four = models.CharField(max_length=200, blank=True)
    vocab_four_mean = models.TextField(blank=True)
    vocab_five = models.CharField(max_length=200, blank=True)
    vocab_five_mean = models.TextField(blank=True)
    
    def __str__ (self):
        return self.headtitle
    
    
    
    
from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# class Categories(models.TextChoices):
#     ENGLISH = 'english',
#     GERMAN = 'german',
#     TURKISH = 'turkish',
#     FRENCH = 'french',
#     RUSSIAN = 'russian',
#     UKRAINIAN = 'ukranian',
#     SPANISH = 'spanish',
#     ARABIC = 'arabic',
#     ROMANIAN = 'romanian',
#     CHINESE = 'chinese'


class Levels(models.TextChoices):
    A1 = 'A1',
    A2 = 'A2',
    B1 = 'B1',
    B2 = 'B2',
    C1 = 'C1',


class Language(models.Model):
    headtitle = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    # category = models.CharField(max_length=50, choices = Categories.choices, default = Categories.ENGLISH)
    level = models.CharField(
        max_length=2, choices=Levels.choices, default=Levels.A1)
    image = models.CharField(
        max_length=1000, default="https://images.pexels.com/photos/5088008/pexels-photo-5088008.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260")
    excerpt = models.CharField(max_length=300, blank=True)
    published = models.BooleanField(default=False)
    day = models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=300, blank=True)
    text_content = models.TextField(blank=True)
    vocab_one = models.CharField(max_length=200, blank=True)
    vocab_one_mean = models.TextField(blank=True)
    vocab_two = models.CharField(max_length=200, blank=True)
    vocab_two_mean = models.TextField(blank=True)
    vocab_three = models.CharField(max_length=200, blank=True)
    vocab_three_mean = models.TextField(blank=True)
    vocab_four = models.CharField(max_length=200, blank=True)
    vocab_four_mean = models.TextField(blank=True)
    vocab_five = models.CharField(max_length=200, blank=True)
    vocab_five_mean = models.TextField(blank=True)
    grammer = models.CharField(max_length=300, blank=True)
    grammer_content = models.TextField(blank=True)
    example_one = models.TextField(blank=True)
    example_two = models.TextField(blank=True)
    example_three = models.TextField(blank=True)
    example_four = models.TextField(blank=True)
    example_five = models.TextField(blank=True)
    writing = models.CharField(max_length=300, blank=True)
    writing_content = models.TextField(blank=True)
    listening = models.CharField(max_length=300, blank=True)
    listening_content = models.TextField(blank=True)

    def __str__(self):
        return self.headtitle

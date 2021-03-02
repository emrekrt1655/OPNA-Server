from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Subscriber
from rest_framework.authtoken.models import Token
from opna.utils import get_random_code
from django.template.defaultfilters import slugify



        
@receiver(pre_save, sender=Subscriber)
def pre_save_create_code(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            get_random_code()+ " " + get_random_code())
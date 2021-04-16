from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Language
from opna.utils import get_random_code


@receiver(pre_save, sender=Language)
def pre_save_create_code(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            instance.excerpt + " " + get_random_code())

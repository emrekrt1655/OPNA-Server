from django.db.models import fields
from rest_framework import serializers
from .models import Subscriber
from rest_framework.validators import UniqueValidator

class SubscriberSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Subscriber.objects.all())]
    )
    
    class Meta:
        model = Subscriber
        fields = ('name', 'surname', 'email', 'subscription', 'subscriber_count')
from django.db.models import fields
from rest_framework import serializers
from .models import Subscriber
from rest_framework.validators import UniqueValidator


class RegisterUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Subscriber.objects.all())]
    )

    class Meta:
        model = Subscriber
        fields = ('name', 'surname', 'email', 'subscription')
        
    


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('name', 'surname', 'email', 'subscription', 'subscriber_count', 'detail_url')
    
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='detail-subscriber',
        lookup_field='slug'
    )
    
        
    
class SubscriberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('name', 'surname', 'email', 'subscription', 'slug', 'update_url', 'delete_url')
        lookup_field = 'slug'
        
    update_url = serializers.HyperlinkedIdentityField(
        view_name='subscriber-update',
        lookup_field='slug'
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name='subscriber-delete',
        lookup_field='slug'
    )
    
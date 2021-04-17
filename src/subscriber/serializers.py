from django.db.models import fields
from rest_framework import serializers
from .models import Subscriber
from rest_framework.validators import UniqueValidator


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('name', 'surname', 'email', 'level',
                  'subscriber_count', 'date_created', 'detail_url')

    detail_url = serializers.HyperlinkedIdentityField(
        view_name='detail-subscriber',
        lookup_field='slug'
    )
    # level_url = serializers.HyperlinkedIdentityField(
    #     view_name='level-list',
    #     lookup_field='slug'
    # )


class RegisterUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Subscriber.objects.all())]
    )

    class Meta:
        model = Subscriber
        fields = ('name', 'surname', 'email', 'level')


class SubscriberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('name', 'surname', 'email', 'level',
                  'slug', 'update_url', 'delete_url')
        lookup_field = 'slug'

    update_url = serializers.HyperlinkedIdentityField(
        view_name='subscriber-update',
        lookup_field='slug'
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name='subscriber-delete',
        lookup_field='slug'
    )

from rest_framework import serializers
from .models import Dialog
from django.db.models import Q


class DialogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialog
        fields = ['detail_url', 'headtitle', 'slug', 'place', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created',  'dialog_content',
                  'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean']
        lookup_field = 'slug'

    detail_url = serializers.HyperlinkedIdentityField(
        view_name='detailed-dialog',
        lookup_field='slug'
    )


class DialogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialog
        fields = ['update_url', 'delete_url', 'headtitle', 'slug', 'place', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'dialog_content',
                  'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean']
        lookup_field = 'slug'
    update_url = serializers.HyperlinkedIdentityField(
        view_name='update',
        lookup_field='slug'
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name='delete',
        lookup_field='slug'
    )


class DialogCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialog
        fields = ['headtitle', 'slug', 'image', 'place', 'excerpt',  'published', 'day', 'month', 'year', 'date_created', 'dialog_content',
                  'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean']

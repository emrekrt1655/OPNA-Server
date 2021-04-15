from rest_framework import serializers
from .models import Tale
from django.db.models import Q

class TaleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tale
        fields = ['detail_url', 'headtitle', 'slug', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'tale_content',
                  'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean']
        lookup_field = 'slug'

    detail_url = serializers.HyperlinkedIdentityField(
        view_name='detailed-bible',
        lookup_field='slug'
    )
    
class TaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tale
        fields = ['update_url', 'delete_url', 'headtitle', 'slug', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'tale_content',
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
    
class TaleCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tale
        fields = ['headtitle', 'slug', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'tale_content',
                  'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean']
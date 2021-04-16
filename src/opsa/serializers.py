from rest_framework import serializers
from .models import Story
from django.db.models import Q

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Story
        fields = ['detail_url', 'headtitle', 'slug', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'story_content',
                  'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean']
        lookup_field = 'slug'

    detail_url = serializers.HyperlinkedIdentityField(
        view_name='detailed-Story',
        lookup_field='slug'
    )
    
class StoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= Story
        fields = ['update_url', 'delete_url', 'headtitle', 'slug', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'story_content',
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
    
class StoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['headtitle', 'slug', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'story', 'story_content',
                  'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean']
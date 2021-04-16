from rest_framework import serializers
from .models import Language
from django.db.models import Q

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model= Language
        fields = ['detail_url', 'level_url', 'headtitle', 'slug', 'level', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'text', 'text_content',
                  'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean',
                  'grammer', 'grammer_content', 'example_one', 'example_two', 'example_three', 'example_four', 'example_five', 'writing', 'writing_content', 'listening', 'listening_content' ]
        lookup_field = 'slug'

    detail_url = serializers.HyperlinkedIdentityField(
        view_name='detailed-language',
        lookup_field='slug'
    )
    level_url = serializers.HyperlinkedIdentityField(
        view_name='level-list',
        lookup_field='slug'
    )
    
class LanguageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= Language
        fields = ['update_url', 'delete_url', 'headtitle', 'slug', 'level', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'text', 'text_content',
                'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean',
                'grammer', 'grammer_content', 'example_one', 'example_two', 'example_three', 'example_four', 'example_five', 'writing', 'writing_content', 'listening', 'listening_content']
        lookup_field = 'slug'
    update_url = serializers.HyperlinkedIdentityField(
        view_name='update',
        lookup_field='slug'
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name='delete',
        lookup_field='slug'
    )
    
class LanguageCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['headtitle', 'slug', 'level', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'text', 'text_content',
                  'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean'
                  'grammer', 'grammer_content', 'example_one', 'example_two', 'example_three', 'example_four', 'example_five', 'writing', 'writing_content', 'listening', 'listening_content']
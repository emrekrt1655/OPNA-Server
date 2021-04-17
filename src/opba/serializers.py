from rest_framework import serializers
from .models import Bible
from django.db.models import Q


class BibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bible
        fields = ['detail_url', 'headtitle', 'slug', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'chapter', 'chapter_content',
                  'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean']
        lookup_field = 'slug'

    detail_url = serializers.HyperlinkedIdentityField(
        view_name='detailed-bible',
        lookup_field='slug'
    )


class BibleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bible
        fields = ['update_url', 'delete_url', 'headtitle', 'slug', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'chapter', 'chapter_content',
                  'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean']
        lookup_field = 'slug'
    update_url = serializers.HyperlinkedIdentityField(
        view_name='update-bible',
        lookup_field='slug'
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name='delete-bible',
        lookup_field='slug'
    )


class BibleCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bible
        fields = ['headtitle', 'slug', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'chapter', 'chapter_content',
                  'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean']

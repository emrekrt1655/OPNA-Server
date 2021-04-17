from rest_framework import serializers
from .models import News
from django.db.models import Q


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['detail_url', 'headtitle', 'slug', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'newstitle_one', 'news_one_content', 'newstitle_two', 'news_two_content', 'newstitle_three', 'news_three_content', 'newstitle_four',
                  'news_four_content', 'newstitle_five', 'news_five_content', 'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean']
        lookup_field = 'slug'

    detail_url = serializers.HyperlinkedIdentityField(
        view_name='detailed-news',
        lookup_field='slug'
    )


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['update_url', 'delete_url', 'headtitle', 'slug', 'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'newstitle_one', 'news_one_content', 'newstitle_two', 'news_two_content', 'newstitle_three', 'news_three_content', 'newstitle_four',
                  'news_four_content', 'newstitle_five', 'news_five_content', 'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean']
        lookup_field = 'slug'
    update_url = serializers.HyperlinkedIdentityField(
        view_name='update',
        lookup_field='slug'
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name='delete',
        lookup_field='slug'
    )


class NewsCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['headtitle', 'slug',  'image', 'excerpt', 'published', 'day', 'month', 'year', 'date_created', 'newstitle_one', 'news_one_content', 'newstitle_two', 'news_two_content', 'newstitle_three', 'news_three_content', 'newstitle_four',
                  'news_four_content', 'newstitle_five', 'news_five_content', 'vocab_one', 'vocab_one_mean', 'vocab_two', 'vocab_two_mean', 'vocab_three', 'vocab_three_mean', 'vocab_four', 'vocab_four_mean', 'vocab_five', 'vocab_five_mean']

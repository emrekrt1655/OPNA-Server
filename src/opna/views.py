from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import News
from .serializers import *
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .pagination import MyPagination


class NewsListView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.order_by('-date_created').filter(published=True)
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    pagination_class = MyPagination


class NewsCategoryView(ListAPIView):
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        category = self.kwargs["category"]
        queryset = News.objects.filter(category__iexact=category)
        return queryset


class NewsDetailView(RetrieveAPIView):
    queryset = News.objects.order_by('-date_created')
    serializer_class = NewsDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]


class NewsCreateApiView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = News.objects.all()
    serializer_class = NewsCreateUpdateSerializer


class NewsDeleteApiView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = 'slug'


class NewsUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = News.objects.all()
    serializer_class = NewsCreateUpdateSerializer
    lookup_field = 'slug'

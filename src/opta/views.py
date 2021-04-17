from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Tale
from .serializers import *
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from opna.pagination import MyPagination


class TaleListView(ListAPIView):
    serializer_class = TaleSerializer
    queryset = Tale.objects.order_by('-date_created').filter(published=True)
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    pagination_class = MyPagination

# class BibleCategoryView(ListAPIView):
#     serializer_class = BibleSerializer
#     permission_classes = [AllowAny]

#     def get_queryset(self):
#         category = self.kwargs["category"]
#         queryset = Bible.objects.filter(category__iexact=category)
#         return queryset


class TaleDetailView(RetrieveAPIView):
    queryset = Tale.objects.order_by('-date_created')
    serializer_class = TaleDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]


class TaleCreateApiView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Tale.objects.all()
    serializer_class = TaleCreateUpdateSerializer


class TaleDeleteApiView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Tale.objects.all()
    serializer_class = TaleDetailSerializer
    lookup_field = 'slug'


class TaleUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Tale.objects.all()
    serializer_class = TaleCreateUpdateSerializer
    lookup_field = 'slug'

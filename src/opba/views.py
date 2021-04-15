from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Bible
from .serializers import *
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from opna.pagination import MyPagination

class BibleListView(ListAPIView):
    serializer_class = BibleSerializer
    queryset = Bible.objects.order_by('-date_created').filter(published=True)
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

class BibleDetailView(RetrieveAPIView):
    queryset = Bible.objects.order_by('-date_created')
    serializer_class = BibleDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    

class BibleCreateApiView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Bible.objects.all()
    serializer_class = BibleCreateUpdateSerializer
    
class BibleDeleteApiView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Bible.objects.all()
    serializer_class = BibleDetailSerializer
    lookup_field = 'slug'


class BibleUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Bible.objects.all()
    serializer_class = BibleCreateUpdateSerializer
    lookup_field = 'slug'
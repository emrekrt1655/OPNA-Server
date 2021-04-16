from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Story
from .serializers import *
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from opna.pagination import MyPagination

class StoryListView(ListAPIView):
    serializer_class = StorySerializer
    queryset = Story.objects.order_by('-date_created').filter(published=True)
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    pagination_class = MyPagination
    
# class StoryCategoryView(ListAPIView):
#     serializer_class = StorySerializer
#     permission_classes = [AllowAny]

#     def get_queryset(self):
#         category = self.kwargs["category"]
#         queryset = Story.objects.filter(category__iexact=category)
#         return queryset

class StoryDetailView(RetrieveAPIView):
    queryset = Story.objects.order_by('-date_created')
    serializer_class = StoryDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    

class StoryCreateApiView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Story.objects.all()
    serializer_class = StoryCreateUpdateSerializer
    
class StoryDeleteApiView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Story.objects.all()
    serializer_class = StoryDetailSerializer
    lookup_field = 'slug'


class StoryUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Story.objects.all()
    serializer_class = StoryCreateUpdateSerializer
    lookup_field = 'slug'
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Subscriber
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterUpdateSerializer, SubscriberSerializer, SubscriberDetailSerializer
from rest_framework.permissions import IsAdminUser, AllowAny


class SubscriberCreateApiView(generics.CreateAPIView):
    queryset = Subscriber.objects.all()
    permissions_classes = [AllowAny]
    serializers_class = RegisterUpdateSerializer
    
class SubscriberListView(generics.ListAPIView):
    queryset = Subscriber.objects.all()
    permissions_classes = [IsAdminUser]
    serializers_class = SubscriberSerializer

class SubscriberCategoryListView(generics.ListAPIView):
    serializer_class = SubscriberSerializer
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        subscription = self.kwargs["subscription"]
        queryset = Subscriber.objects.filter(subscription__iexact=subscription)
        return queryset


class SubscriberDetailView(generics.RetrieveAPIView):
    queryset = Subscriber.objects.all()
    permissions_classes = [IsAdminUser]
    serializers_class =[SubscriberDetailSerializer]
    
class SubscriberUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Subscriber.objects.all()
    permissions_classes = [IsAdminUser]
    lookup_field = 'slug'
    serializers_class = RegisterUpdateSerializer
    
    def perform_update(self, serializer):
        serializer.save()
        
class SubscriberDeleteApiView(generics.DestroyAPIView):
    permissions_classes = [IsAdminUser]
    queryset = Subscriber.objects.all()
    serializers_class =[SubscriberDetailSerializer]
    lookup_field = 'slug'
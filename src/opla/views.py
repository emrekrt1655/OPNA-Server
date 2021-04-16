from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Language
from .serializers import *
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from opna.pagination import MyPagination

class LanguageListView(ListAPIView):
    serializer_class = LanguageSerializer
    queryset = Language.objects.order_by('-date_created').filter(published=True)
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    pagination_class = MyPagination
    
# class LanguageCategoryView(ListAPIView):
#     serializer_class = LanguageSerializer
#     permission_classes = [AllowAny]

#     def get_queryset(self):
#         category = self.kwargs["category"]
#         queryset = Language.objects.filter(category__iexact=category)
#         return queryset

class LanguageLevelView(ListAPIView):
    serializer_class = LanguageSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        level = self.kwargs["level"]
        queryset = Language.objects.filter(level__iexact=level)
        return queryset

class LanguageDetailView(RetrieveAPIView):
    queryset = Language.objects.order_by('-date_created')
    serializer_class = LanguageDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    

class LanguageCreateApiView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Language.objects.all()
    serializer_class = LanguageCreateUpdateSerializer
    
class LanguageDeleteApiView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Language.objects.all()
    serializer_class = LanguageDetailSerializer
    lookup_field = 'slug'


class LanguageUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Language.objects.all()
    serializer_class = LanguageCreateUpdateSerializer
    lookup_field = 'slug'
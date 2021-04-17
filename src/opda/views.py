from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Dialog
from .serializers import *
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from opna.pagination import MyPagination


class DialogListView(ListAPIView):
    serializer_class = DialogSerializer
    queryset = Dialog.objects.order_by('-date_created').filter(published=True)
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    pagination_class = MyPagination

# class DialogCategoryView(ListAPIView):
#     serializer_class = DialogSerializer
#     permission_classes = [AllowAny]

#     def get_queryset(self):
#         category = self.kwargs["category"]
#         queryset = Dialog.objects.filter(category__iexact=category)
#         return queryset


class DialogPlaceListView(ListAPIView):
    serializer_class = DialogSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        place = self.kwargs["place"]
        queryset = Dialog.objects.filter(place__iexact=place)
        return queryset


class DialogDetailView(RetrieveAPIView):
    queryset = Dialog.objects.order_by('-date_created')
    serializer_class = DialogDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]


class DialogCreateApiView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Dialog.objects.all()
    serializer_class = DialogCreateUpdateSerializer


class DialogDeleteApiView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Dialog.objects.all()
    serializer_class = DialogDetailSerializer
    lookup_field = 'slug'


class DialogUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Dialog.objects.all()
    serializer_class = DialogCreateUpdateSerializer
    lookup_field = 'slug'

from django.urls import path
from .views import SubscriberListView, SubscriberCategoryListView, SubscriberDeleteApiView
from rest_framework import views as rest_views

urlpatterns = [
    path('list/', SubscriberListView.as_view(), name='subscriber-list'),
    path('list/<subscription>', SubscriberCategoryListView.as_view(), name='subscriber-category-list'),
    path('delete/<slug>', SubscriberDeleteApiView.as_view(), name='subscriber-delete')
]
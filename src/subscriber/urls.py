from django.urls import path
from .views import SubscriberListView, SubscriberCategoryListView, SubscriberCategoryLevelListView, SubscriberDeleteApiView, SubscriberCreateApiView, SubscriberUpdateApiView, SubscriberDetailView
from rest_framework import views as rest_views

urlpatterns = [
    path('list/', SubscriberListView.as_view(), name='subscriber-list'),
    # path('list/<subscription>/', SubscriberCategoryListView.as_view(), name='subscriber-category-list'),
    path('list/<subscriptionLevel>/', SubscriberCategoryLevelListView.as_view(), name='subscriber-category-level-list'),
    path('delete/<slug>/', SubscriberDeleteApiView.as_view(), name='subscriber-delete'),
    path('create/', SubscriberCreateApiView.as_view(), name='create'),
    path('update/<slug>/', SubscriberUpdateApiView.as_view(), name='subscriber-update'),
    path('detailed/<slug>/', SubscriberDetailView.as_view(), name='detail-subscriber'),
]
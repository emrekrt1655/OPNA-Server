from django.urls import path
from .views import *

urlpatterns = [
    path('list/', NewsListView.as_view(), name='list'),
    path('list/<category>/', NewsCategoryView.as_view(), name='category_list'),
    path('create/', PostCreateApiView.as_view(), name='create'),
    path('list/detail/<slug>/', NewsDetailView.as_view(), name='detailed_news'),
    path('list/detail/<slug>/delete/',
         NewsDeleteApiView.as_view(), name='update'),
    path('list/detail/<slug>/update/',
         NewsUpdateApiView.as_view(), name='delete'),


]

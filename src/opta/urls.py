from django.urls import path
from .views import *

urlpatterns = [
    path('list/', TaleListView.as_view(), name="list"),
    #     path('list/<category>/', BibleCategoryView.as_view(), name='category_list'),
    path('list/detail/<slug>/', TaleDetailView.as_view(), name='detailed-tale'),
    path('create/', TaleCreateApiView.as_view(), name='create'),
    path('list/detail/<slug>/delete/',
         TaleDeleteApiView.as_view(), name='delete-tale'),
    path('list/detail/<slug>/update/',
         TaleUpdateApiView.as_view(), name='update-tale'),

]

from django.urls import path
from .views import *

urlpatterns = [
    path('list/', StoryListView.as_view(), name="list"),
    #     path('list/<category>/', StoryCategoryView.as_view(), name='category_list'),
    path('list/detail/<slug>/', StoryDetailView.as_view(), name='detailed-Story'),
    path('list/detail/<slug>/delete/',
         StoryDeleteApiView.as_view(), name='delete'),
    path('list/detail/<slug>/update/',
         StoryUpdateApiView.as_view(), name='update'),

]
from django.urls import path
from .views import *

urlpatterns = [
    path('list/', BibleListView.as_view(), name="list"),
    #     path('list/<category>/', BibleCategoryView.as_view(), name='category_list'),
    path('create/', BibleCreateApiView.as_view(), name='create'),

    path('list/detail/<slug>/', BibleDetailView.as_view(), name='detailed-bible'),
    path('list/detail/<slug>/delete/',
         BibleDeleteApiView.as_view(), name='delete-bible'),
    path('list/detail/<slug>/update/',
         BibleUpdateApiView.as_view(), name='update-bible'),

]

from django.urls import path
from .views import *

urlpatterns = [
    path('list/', DialogListView.as_view(), name="list"),
    #     path('list/<category>/', DialogCategoryView.as_view(), name='category_list'),
    path('list/<place>/', DialogPlaceListView.as_view(), name='place-list'),
    path('list/detail/<slug>/', DialogDetailView.as_view(), name='detailed-dialog'),
    path('list/detail/<slug>/delete/',
         DialogDeleteApiView.as_view(), name='delete'),
    path('list/detail/<slug>/update/',
         DialogUpdateApiView.as_view(), name='update'),

]
from django.urls import path
from .views import *

urlpatterns = [
    path('list/', LanguageListView.as_view(), name="list"),
    #     path('list/<category>/', LanguageCategoryView.as_view(), name='category_list'),
    path('list/<level>/', LanguageLevelView.as_view(), name='level-list'),
    path('list/detail/<slug>/', LanguageDetailView.as_view(), name='detailed-Language'),
    path('list/detail/<slug>/delete/',
         LanguageDeleteApiView.as_view(), name='delete'),
    path('list/detail/<slug>/update/',
         LanguageUpdateApiView.as_view(), name='update'),

]
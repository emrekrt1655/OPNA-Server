from django.urls import path
from .views import *

urlpatterns = [
    path('list/', LanguageListView.as_view(), name="list"),
    #     path('list/<category>/', LanguageCategoryView.as_view(), name='category_list'),
    path('create/', LanguageCreateApiView.as_view(), name='create'),
    path('list/level/<level>/', LanguageLevelView.as_view(), name='level_list'),
    path('list/detail/<slug>/', LanguageDetailView.as_view(),
         name='detailed-language'),
    path('list/detail/<slug>/delete/',
         LanguageDeleteApiView.as_view(), name='delete-language'),
    path('list/detail/<slug>/update/',
         LanguageUpdateApiView.as_view(), name='update-language'),

]

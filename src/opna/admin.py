from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News

class NewsAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    list_display = ( 'id' , 'headtitle', 'category', 'date_created' )
    list_display_links = ('id', 'headtitle')
    search_fields = ('headtitle', 'category' )
    list_per_page = 25
    summernote_fields = ('content',)
    
admin.site.register(News, NewsAdmin)

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Story

class StoryAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    list_display = ( 'id' , 'headtitle',  'date_created' )
    list_display_links = ('id', 'headtitle')
    search_fields = ('headtitle',  )
    list_per_page = 25
    summernote_fields = ('content',)
    
admin.site.register(Story, StoryAdmin)
from django.contrib import admin
from .models import Song
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Song)
class SongAdmin(SummernoteModelAdmin):

    list_display = ('title', 'id', 'composer', 'arranger')
    search_fields = ['title', 'composer', 'arranger']
    list_filter = ('title', 'composer', 'arranger')
    summernote_fields = ('info',)


# Register your models here.

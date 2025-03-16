from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Song


@admin.register(Song)
class SongAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters and rich-text editor.
    """
    list_display = ('title', 'id', 'composer', 'arranger', 'musician')
    search_fields = ['title', 'composer', 'arranger']
    list_filter = ('title', 'composer', 'arranger')
    summernote_fields = ('info',)


# Register your models here.

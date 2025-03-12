from django.shortcuts import render
from django.views import generic
from .models import Song

# Create your views here.


class SongList(generic.ListView):
   queryset = Song.objects.all()
   template_name = "song_list.html"

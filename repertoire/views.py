from django.shortcuts import render
from django.views import generic
from .models import Song
from .forms import AddSongForm

# Create your views here.


# class SongList(generic.ListView):
#    queryset = Song.objects.all()
#    template_name = "song_list.html"

def SongList(request):

   queryset = Song.objects.all()
   songs = queryset

   if request.method == "POST":
    add_song_form = AddSongForm(data=request.POST)
    if add_song_form.is_valid():
        song = add_song_form.save(commit=False)
        song.musician = request.user
        song.save()

   add_song_form = AddSongForm()

   return render(
      request,
      "repertoire/song_list.html",
      {
         "songs": songs,
         "add_song_form": add_song_form,
      },
   )


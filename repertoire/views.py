from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Song
from .forms import AddSongForm

# Create your views here.


# class SongList(generic.ListView):
#    queryset = Song.objects.all()
#    template_name = "song_list.html"

def song_list(request):

   queryset = Song.objects.all()
   songs = queryset

   if request.method == "POST":
      add_song_form = AddSongForm(data=request.POST)
      if add_song_form.is_valid():
         song = add_song_form.save(commit=False)
         song.musician = request.user
         song.save()
         messages.add_message(
            request, messages.SUCCESS,
            'Song added!'
    )

   add_song_form = AddSongForm()

   return render(
      request,
      "repertoire/song_list.html",
      {
         "songs": songs,
         "add_song_form": add_song_form,
      },
   )

def song_rehearsal(request, id):
    
   # queryset = Song.objects.filter(musician==User)
   queryset = Song.objects.all()
   song = get_object_or_404(queryset, id=id)

   return render(
      request,
      "repertoire/song_rehearsal.html",
      {
         "song": song,
      },
   )



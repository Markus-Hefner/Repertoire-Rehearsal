from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
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


def song_edit(request, id):
   # queryset = Song.objects.all()
   # song = get_object_or_404(queryset, id=id)

   song = Song.objects.get(pk=id)
   add_song_form = AddSongForm(request.POST or None, instance=song)

   if request.method == "POST":
      if add_song_form.is_valid() and song.musician == request.user:
         add_song_form.save()
         messages.add_message(request, messages.SUCCESS, 'Edit successful!')
         return HttpResponseRedirect(reverse('song_rehearsal', args=[id]))
      else:
         messages.add_message(request, messages.ERROR,
                              'Sorry, edit failed. Please try again!')
         return HttpResponseRedirect(reverse('song_rehearsal', args=[id]))
   
   return render(
      request,
      "repertoire/song_edit.html",
      {
         "song": song,
         "add_song_form": add_song_form,
      },
   )


def song_delete_warning(request, id):
   song = Song.objects.get(pk=id)

   return render(
      request,
      "repertoire/song_delete_warning.html",
      {
         "song": song,
      },
   )


def song_delete(request, id):
   song = Song.objects.get(pk=id)

   if song.musician == request.user:
      song.delete()
      messages.add_message(request, messages.SUCCESS, 'Song deleted!')
      return redirect('repertoire')
   else:
      messages.add_message(request, messages.ERROR,
                           'Sorry, you are not authorized to delete this song!')
      return redirect('repertoire')
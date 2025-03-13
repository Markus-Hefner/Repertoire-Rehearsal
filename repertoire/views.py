from django.shortcuts import render, get_object_or_404, reverse
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


@login_required
def song_edit(request, id):
   """
   View to edit songs
   """
   if request.method == "POST":

      queryset = Song.objects.filter(user=request.user)
      song = get_object_or_404(queryset, id=id)
      comment = get_object_or_404(Comment, pk=comment_id)
      add_song_form = AddSongForm(data=request.POST, instance=song)

      if add_song_form.is_valid() and song.musician == request.user:
         song = add_song_form.save(commit=False)
         comment.save()
         messages.add_message(request, messages.SUCCESS, 'Changes saved!')
      else:
         messages.add_message(request, messages.ERROR, 'Sorry, could not save changes.')

   return HttpResponseRedirect(reverse('song_rehearsal', args=[id]))

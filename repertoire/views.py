from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Song
from .forms import AddSongForm

# Create your views here.


def song_list(request):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts.
    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.

    **Template:**

    :template:`blog/index.html`
    """
    """
    If user is logged in:
        Returns an instance of :form:`repertoire.AddSongForm`
        and displays it.

        Displays all by this user added songs in a list.

    If user is not logged in:
        Displays no form and no songs.
        Displays the alternative text from the HTML template.

    **Context**

    If user is logged in:
        ``songs``
            An ordered list of all instances of :model:`repertoire.Song`
        ``add_song_form``
            An instance of :form:`repertoire.AddSongForm`

    If user is not logged in:
        No context, just the template.

    **Template:**

    If user is logged in or not:
        :template:`repertoire.song_list.html`
    """
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

    if not request.user.is_authenticated:
        return render(
            request,
            "repertoire/song_list.html"
        )
    else:
        queryset = Song.objects.all().order_by("title")
        songs = queryset
        return render(
            request,
            "repertoire/song_list.html",
            {
                "songs": songs,
                "add_song_form": add_song_form,
            },
        )


@login_required
def song_rehearsal(request, id):
    """
    Displays an instance of :model:`repertoire.Song`

    **Context**

    ``song``
        An individual instance of :model:`repertoire.Song`

    **Template:**

    :template:`repertoire.song_rehearsal.html`
    """
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
    Displays an individual instance of :model:`repertoire.Song`
    for editing and updating the database.

    **Context**

    ``song``
        An individual instance of :model:`repertoire.Song`
    ``add_song_form``
        An instance of :form:`repertoire.AddSongForm`

    **Template**

    :template:`repertoire.song_edit.html`
    """
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


@login_required
def song_delete_warning(request, id):
    """
    Displays an individual instance of :model:`repertoire.Song`
    to varify deletion.

    **Context**

    ``song``
        An individual instance of :model:`repertoire.Song`

    **Template**

    :template:`repertoire.song_delete_warning.html`
    """
    song = Song.objects.get(pk=id)

    return render(
        request,
        "repertoire/song_delete_warning.html",
        {
            "song": song,
        },
    )


@login_required
def song_delete(request, id):
    """
    Deletes an individual instance of :model:`repertoire.Song`
    from the database.

    **Context**

    None

    **Template**

    None
    """
    song = Song.objects.get(pk=id)

    if song.musician == request.user:
        song.delete()
        messages.add_message(request, messages.SUCCESS, 'Song deleted!')
        return redirect('repertoire')
    else:
        messages.add_message(request, messages.ERROR,
                             'You are not authorised to delete this song!')
        return redirect('repertoire')

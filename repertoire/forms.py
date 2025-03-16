from django import forms
from .models import Song


class AddSongForm(forms.ModelForm):
    """
    Form class for users to add songs.
    """
    class Meta:
        model = Song
        fields = ('title', 'composer', 'arranger', 'info', 'target_bpm')

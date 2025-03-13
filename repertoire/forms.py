from .models import Song
from django import forms


class AddSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'composer', 'arranger', 'info')
from django import forms
from .models import Song


class AddSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'composer', 'arranger', 'info', 'target_bpm')

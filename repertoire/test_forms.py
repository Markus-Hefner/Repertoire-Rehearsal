from django.test import TestCase
from .forms import AddSongForm

# Create your tests here.


class TestAddSongFormTitle(TestCase):

    def test_form_is_valid(self):
        """ Test for required field """
        add_song_form = AddSongForm({'title': 'This is the best Song ever'})
        self.assertTrue(add_song_form.is_valid(), msg="Form is not valid")


class TestAddSongFormTitleFailing(TestCase):

    def test_form_is_invalid(self):
        """ Test for required field (field not provided -> should fail)"""
        add_song_form = AddSongForm({'title': ''})
        self.assertTrue(add_song_form.is_valid(), msg="Form is not valid")


class TestAddSongFormFourFields(TestCase):

    def test_form_is_valid(self):
        """ Test for four fields"""
        form = AddSongForm({
            'title': 'Best song ever',
            'composer': 'Best band ever',
            'arranger': 'This song is perfect as is',
            'info': 'There is nothing to say. Just - perfect!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

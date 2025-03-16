from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import AddSongForm
from .models import Song

# Create your tests here.


class Test(TestCase):

    def setUp(self):
        """Create a superuser and a song"""
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.song = Song(title="Best song ever", composer="Best band ever",
                         arranger="Original", info="",
                         musician=self.user, target_bpm="115")
        self.song.save()
        
    def test_render_song_list_page_with_add_song_form(self):
        """
        Test for rendering the correct template with the correct songs
        for the logged-in user
        """
        self.client.login(username="myUsername", password="myPassword")
        response = self.client.get(reverse(
            'repertoire'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Best song ever", response.content)
        self.assertIn(b"Best band ever", response.content)
        self.assertIn(b"Original", response.content)
        self.assertIsInstance(
            response.context['add_song_form'], AddSongForm)
        
    def test_adding_song(self):
        """Test for adding a new song"""
        self.client.login(username="myUsername", password="myPassword")
        song_add = {
            'title': 'Another awesome Song'
            }
        response = self.client.post(reverse(
            'repertoire'), song_add)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Another awesome Song", response.content)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    """
    Stores a single song entry related to the "auth.User"-model.
    """
    title = models.CharField(max_length=150,)
    composer = models.CharField(max_length=150, blank=True)
    arranger = models.CharField(max_length=150, blank=True)
    info = models.TextField(blank=True)
    musician = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="songs"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    target_bpm = models.IntegerField(null=True, blank=True)
    next_due_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.title} | by {self.composer} | arranged by {self.arranger}"

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=150, unique=True)
    composer = models.CharField(max_length=150,)
    arranger = models.CharField(max_length=150, default="This is the original version")
    info = models.TextField(blank=True)
    musician = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="songs"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    bpm = models.IntegerField(null=True)
    next_due_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.title} | by {self.composer} | arranged by {self.arranger}"

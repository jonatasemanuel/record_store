from django.db import models
from django.utils import timezone


# Create your models here.
class Disc(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.title


class Credits(models.Model):
    disc = models.ForeignKey(Disc, on_delete=models.DO_NOTHING)
    artist = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    release = models.DateTimeField(default=timezone.now)
    show = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.artist

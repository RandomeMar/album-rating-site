from django.db import models


class Artists(models.Model):
    name = models.CharField(max_length=250)
    # TODO: Want to store an image somehow

class Albums(models.Model):
    name = models.CharField(max_length=250)
    # TODO: Want to store an image somehow
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)

class Songs(models.Model):
    name = models.CharField(max_length=250)
    album = models.ForeignKey(Albums, models.CASCADE)
    album_pos = models.PositiveIntegerField()
from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=255)
    code = models.SlugField(max_length=20)
    synopsis = models.TextField()
    cover_art_height = models.IntegerField()
    cover_art_width = models.IntegerField()
    cover_art = models.ImageField(upload_to='cover_art', height_field='cover_art_height', width_field='cover_art_width')

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=255)
    code = models.SlugField(max_length=20)
    lyrics = models.TextField()
    album = models.ForeignKey(Album)

    def __str__(self):
        return self.title
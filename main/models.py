from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=255)
    code = models.SlugField(max_length=50)
    synopsis = models.TextField()
    cover_art_height = models.IntegerField()
    cover_art_width = models.IntegerField()
    cover_art = models.ImageField(upload_to='cover_art', height_field='cover_art_height', width_field='cover_art_width')

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=255)
    code = models.SlugField(max_length=50)
    lyrics = models.TextField()
    album = models.ForeignKey(Album)
    index = models.IntegerField()
    art_height = models.IntegerField()
    art_width = models.IntegerField()
    art = models.ImageField(upload_to='song_art', height_field='art_height', width_field='art_width')

    class Meta:
        ordering = ['index']

    def __str__(self):
        return self.title

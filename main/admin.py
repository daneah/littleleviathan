from django.contrib import admin

from main.models import Album, Song


class AlbumAdmin(admin.ModelAdmin):
    model = Album

    exclude = ('cover_art_height', 'cover_art_width')
    prepopulated_fields = {'code': ('title',)}


class SongAdmin(admin.ModelAdmin):
    model = Song

admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
from django.contrib import admin

from main.models import Album, Song


class AlbumAdmin(admin.ModelAdmin):
    model = Album

    exclude = ('cover_art_height', 'cover_art_width')
    prepopulated_fields = {'code': ('title',)}

    list_display = ('pk', 'title', 'code', 'synopsis',)
    list_editable = ('title', 'code', 'synopsis',)


class SongAdmin(admin.ModelAdmin):
    model = Song

    exclude = ('art_height', 'art_width')
    prepopulated_fields = {'code': ('title',)}

    list_display = ('pk', 'title', 'code', 'album', 'index',)
    list_editable = ('title', 'code', 'album', 'index',)

admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)

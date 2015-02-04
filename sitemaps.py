from django.contrib.sitemaps import Sitemap

from main.models import Album, Song

class AlbumSitemap(Sitemap):
    changefreq = "never"
    priority = 1.0

    def items(self):
        return Album.objects.all()

class SongSitemap(Sitemap):
    changefreq = "never"
    priority = 0.75

    def items(self):
        return Song.objects.all()

from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from sitemaps import AlbumSitemap, SongSitemap

sitemaps = {
    'albums': AlbumSitemap,
    'songs': SongSitemap,
}

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main.urls', namespace='main')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
)

urlpatterns += staticfiles_urlpatterns()

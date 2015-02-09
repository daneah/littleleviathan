from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
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

if settings.DEBUG:
    urlpatterns += patterns(
        url(r'^404/$', TemplateView.as_view(template_name='404.html'), name='not_found'),
        url(r'^500/$', TemplateView.as_view(template_name='500.html'), name='server_error')
    )

urlpatterns += staticfiles_urlpatterns()

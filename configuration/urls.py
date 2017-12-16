from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from sitemaps import AlbumSitemap, SongSitemap

sitemaps = {
    'albums': AlbumSitemap,
    'songs': SongSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('main.urls')),
    url(r'^sitemap\.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^400/', TemplateView.as_view(template_name='400.html'), name='bad_request'),
        url(r'^403/', TemplateView.as_view(template_name='403.html'), name='permission_denied'),
        url(r'^404/', TemplateView.as_view(template_name='404.html'), name='not_found'),
        url(r'^500/', TemplateView.as_view(template_name='500.html'), name='server_error'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

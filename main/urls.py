from django.conf.urls import url
from django.views.generic import TemplateView

from main.views import HomeView, AlbumListView, AlbumDetailView, SongDetailView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^album/(?P<album_code>[\w\-]+)/song/(?P<song_code>[\w\-]+)/', SongDetailView.as_view(), name='song'),
    url(r'^album/(?P<album_code>[\w\-]+)/', AlbumDetailView.as_view(), name='album'),
    url(r'^albums/', AlbumListView.as_view(), name='albums'),
    url(r'^robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]

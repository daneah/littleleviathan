from django.conf.urls import patterns, url

from main.views import HomeView, AlbumListView, AlbumDetailView, SongDetailView

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^albums/$', AlbumListView.as_view(), name='albums'),
    url(r'^album/(?P<album_code>[\w\-]+)/$', AlbumDetailView.as_view(), name='album'),
    url(r'^album/(?P<album_code>[\w\-]+)/song/(?P<song_code>[\w\-]+)/$', SongDetailView.as_view(), name='song'),
)

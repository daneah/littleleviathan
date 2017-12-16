from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^album/(?P<album_code>[\w\-]+)/song/(?P<song_code>[\w\-]+)/', views.SongDetailView.as_view(), name='song'),
    url(r'^album/(?P<album_code>[\w\-]+)/', views.AlbumDetailView.as_view(), name='album'),
    url(r'^albums/', views.AlbumListView.as_view(), name='albums'),
    url(r'^about/', views.AboutView.as_view(), name='about'),
    url(r'^press/', views.PressView.as_view(), name='press'),
    url(r'^robots.txt', views.TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]

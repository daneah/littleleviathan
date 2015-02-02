from django.views.generic import TemplateView, ListView, DetailView

from main.models import Album, Song


class HomeView(TemplateView):
    template_name = 'main/index.html'


class AlbumListView(ListView):
    model = Album


class AlbumDetailView(DetailView):
    model = Album
    slug_field = 'code'
    slug_url_kwarg = 'album_code'


class SongListView(ListView):
    model = Song


class SongDetailView(DetailView):
    model = Song

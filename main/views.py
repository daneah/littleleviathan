from django.views.generic import TemplateView, ListView, DetailView

from main.models import Album, Song


class HomeView(TemplateView):
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['featured_album'] = Album.objects.get(title='Little Leviathan')
        except Album.DoesNotExist:
            pass
        return context


class AlbumListView(ListView):
    model = Album


class AlbumDetailView(DetailView):
    model = Album
    slug_field = 'code'
    slug_url_kwarg = 'album_code'


class SongDetailView(DetailView):
    model = Song
    slug_field = 'code'
    slug_url_kwarg = 'song_code'

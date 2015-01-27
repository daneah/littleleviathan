from django.conf.urls import patterns, url

from main.views import HomeView

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home')
)
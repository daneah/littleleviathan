from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from main.models import Album


class HomePageTestCase(TestCase):

    def test_home_page_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_album_list_view(self):
        response = self.client.get('/albums/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/album_list.html')

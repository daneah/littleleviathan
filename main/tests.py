from django.test import TestCase


class HomePageTestCase(TestCase):

    def test_home_page_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

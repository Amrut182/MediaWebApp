from django.test import TestCase, SimpleTestCase
from django.test.client import Client
from django.urls import reverse, resolve


'''
    path('', views.home, name='Home'),
    path('download',views.download,name='download'),'''


class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()

    def test_url_name_for_home(self):
        name = reverse('Home')
        path = '/'
        self.assertEqual(path, name)

    def test_url_name_for_download(self):
        name = reverse('download')
        path = '/download'
        self.assertEqual(path, name)

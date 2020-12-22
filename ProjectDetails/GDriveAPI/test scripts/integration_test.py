from django.test import TestCase, SimpleTestCase
from django.test.client import Client
from django.urls import reverse, resolve
from mediaApp.views import *


class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()

    def test_url_name_for_login(self):
        name = reverse('glogin')
        path = '/glogin/'
        self.assertEqual(path, name)

    def test_url_name_for_logout(self):
        name = reverse('glogout')
        path = '/glogout/'
        self.assertEqual(path, name)

    def test_home_resolves_to_download(self):
        response = resolve('/download/')
        self.assertEqual(response.func, download)

    def test_youtube_resolves_to_youtube_query(self):
        response = resolve('/query/')
        self.assertEqual(response.func, youtube_query)

    def test_show_video(self):
        response = resolve('/query/<vid>')
        self.assertEqual(response.func, show_local_video)

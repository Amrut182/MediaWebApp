from django.test import TestCase, SimpleTestCase
from django.test.client import Client
from django.urls import reverse, resolve
from mediaApp.views import home, youtube_query

# urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',mediaApp_views.home,name='home'),
    # path('query/', mediaApp_views.youtube_query, name='youtube_query'),
    # path('query/<int:vid>', mediaApp_views.show_video, name='show_video'),
    # path('signup/',user_views.signup,name='signup'),
    # path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    # path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    # path('oauth/', include('social_django.urls', namespace='social')),
# ]

class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()

    def test_url_name_for_home(self):
        name = reverse('home')
        path = '/'
        self.assertEqual(path, name)

    def test_url_name_for_youtube_query_page(self):
        name = reverse('youtube_query')
        path = '/query/'
        self.assertEqual(path, name)

    def test_home_resolves_to_home_view(self):
        response = resolve('/')
        self.assertEqual(response.func, home)

    def test_youtube_resolves_to_youtube_query(self):
        response = resolve('/query/')
        self.assertEqual(response.func, youtube_query)


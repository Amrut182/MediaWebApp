"""mediaWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from mediaApp import views as mediaApp_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mediaApp_views.home,name='home'),
    path('query/', mediaApp_views.youtube_query, name='youtube_query'),
    path('query/<int:vid>', mediaApp_views.show_video, name='show_video'),
    path('query/<vid>', mediaApp_views.show_local_video, name='show_local_video'),
    path('drivequery/<vid>', mediaApp_views.show_drive_video, name='show_drive_video'),
    path('signup/',user_views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('glogin/', mediaApp_views.glogin, name="glogin"),
    path('glogout/',mediaApp_views.glogout, name="glogout"),
    path('download/', mediaApp_views.download, name='download'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

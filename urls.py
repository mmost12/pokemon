from django.conf.urls import url, include
from django.contrib import admin

from django_nyt.urls import get_pattern as get_nyt_patern

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('homepage.urls')),
]
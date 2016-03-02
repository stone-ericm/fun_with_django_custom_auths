from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from url import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^shorten$', views.UrlShorten.as_view(), name='shorten'),
    url(r'^(?P<key>[A-Za-z0-9\-\_]+)$', views.UrlRedirect.as_view(), name='redirect'),
]

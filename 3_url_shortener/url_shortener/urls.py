from django.conf.urls import url, include
from .views import Index
from url_shortener import views

urlpatterns = [
	url(r'^url/(?P<key>[0-9a-zA-Z]+)', views.short_link, name='url'),
	url(r'^$', Index.as_view(), name='index'),
]

# (?P<key>[^/]+)
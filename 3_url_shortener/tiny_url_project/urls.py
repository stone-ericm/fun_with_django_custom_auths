"""tiny_url_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from url_shortener import views
# from url_shortener import views, Index
# from .views import Index


urlpatterns = [
	url(r'^', include('url_shortener.urls', namespace='url_shortener')),
    # url(r'^(?P<key>.+)', views.short_link, name = 'key'),
	# url(r'^url_shortener/', include('url_shortener.urls', namespace='url_shortener')),
    url(r'^admin/', admin.site.urls),
]

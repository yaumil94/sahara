from django.conf.urls import url
from .views import ViewBaseRegistrasi
from .views import ViewRegistrasi

urlpatterns = [
    url(r'^$', ViewBaseRegistrasi().home, name='home'),
    url(r'^registrasi/$', ViewRegistrasi().registrasi, name='registrasi-member'),

]
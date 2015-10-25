from django.conf.urls import include, url
#from django.contrib import admin
from registrasi.admin import admin_site

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin_site.urls)),
    #url(r'^administrator/', include('administrator.urls', namespace='administrator')),
    url(r'', include('registrasi.urls', namespace='registrasi')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'', include('saharasite.urls', namespace='saharasite')),
]
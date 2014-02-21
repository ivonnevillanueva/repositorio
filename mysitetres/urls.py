from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('polls.views',
    url(r'^$','indice'),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
   
)

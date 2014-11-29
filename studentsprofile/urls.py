from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^profiler/', include('profiler.urls', namespace="profiler")),

    url(r'^admin/', include(admin.site.urls)),
)

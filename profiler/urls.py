from django.conf.urls import url, patterns

from profiler import views

urlpatterns = patterns('',

	url(r'^$', views.index, name='index'),
	url(r'^(?P<student_id>\d+)/$', views.studentid, name='studentid'),
	url(r'^studentdata/$', views.studentdata, name='studentdata'),
	)  

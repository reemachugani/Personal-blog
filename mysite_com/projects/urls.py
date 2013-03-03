from django.conf.urls.defaults import *


urlpatterns = patterns('projects.views',
	url(r'^$', 'projects_home', name='projects_home'),	
	)
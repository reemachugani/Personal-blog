from django.conf.urls.defaults import *

urlpatterns = patterns('links.views',
	url(r'^$', 'links_home', name='links_home'),
	url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive_by_month', name="links_archive_by_month"),
	url(r'^tag/(?P<tag>[-\w]+)/$', 'tag_page', name="links_tag_page"),
	)
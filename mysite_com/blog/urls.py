from django.conf.urls.defaults import *
#from blog.models import Entry


urlpatterns = patterns('blog.views',
	url(r'^$', 'blog_home', name='blog_home'),
	url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive_by_month', name="blog_archive_by_month"),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'entry_detail', name="blog_entry_detail"),
	url(r'^tag/(?P<tag>[-\w]+)/$', 'tag_page', name="blog_tag_page"),
	url(r'^love/(?P<slug>[-\w]+)/$', 'love_inc', name="blog_love"),
	)
from django.conf.urls import patterns, include, url
from MY_SITE import settings
from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^blog/', include('blog.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS}),	
#    url(r'^home/$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}, name="home"),
    (r'^links/', include('links.urls')),
#    url(r'^projects/$', 'django.views.generic.simple.direct_to_template', {'template': 'projects.html'}, name="projects_home"),
    url(r'^$', 'blog.views.blog_home', name='blog_home'),   
)

urlpatterns += staticfiles_urlpatterns()

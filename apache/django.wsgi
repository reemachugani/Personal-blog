import os
import sys

path = '/var/www'
if path not in sys.path:
    sys.path.insert(0, '/var/www')


sys.path.append('/var/www')
sys.path.append('/var/www/mysite')
sys.path.append('/var/www/mysite/mysite_com')
sys.path.append('/var/www/mysite/mysite_com/MY_SITE')


os.environ['DJANGO_SETTINGS_MODULE'] = 'MY_SITE.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

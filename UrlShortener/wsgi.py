import os
import sys



os.environ['DJANGO_SETTINGS_MODULE'] = 'UrlShortener.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = get_wsgi_application()

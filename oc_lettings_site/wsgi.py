"""WSGI config for oc_lettings_site: exposes the WSGI callable as a module-level variable."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_wsgi_application()

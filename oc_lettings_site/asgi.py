"""ASGI config for oc_lettings_site: exposes the ASGI callable as a module-level variable."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_asgi_application()

"""
ASGI config for codelab_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from codelab_backend.settings import base as base_settings

settings_definitions_based_on_debug = {
        True: 'codelab_backend.settings.local',
        False: 'codelab_backend.settings.production',
    }

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 
    settings_definitions_based_on_debug[base_settings.DEBUG]
)

application = get_asgi_application()

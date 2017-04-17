"""
WSGI config for UrlShortener project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)

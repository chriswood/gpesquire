"""
WSGI config for gpesquire project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/chriswood.cool/')
sys.path.append('/var/www/chriswood.cool/gpesquire/')
os.environ['PYTHON_EGG_CACHE'] = '/var/www/chriswood.cool/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

application = get_wsgi_application()

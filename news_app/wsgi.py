"""
WSGI config for news_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""


from django.core.wsgi import get_wsgi_application
import os
import sys


# Add your project directory to the sys.path
path = '/home/phantomprogrammer200/news_app'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_app.settings')

# Activate the virtual environment
activate_this = '/home/phantomprogrammer200/news_app/myenv/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), dict(__file__=activate_this))

application = get_wsgi_application()

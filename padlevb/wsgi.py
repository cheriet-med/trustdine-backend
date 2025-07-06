import os
from django.core.wsgi import get_wsgi_application

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'padlevb.settings')

# Get the WSGI application
application = get_wsgi_application()

# Expose the application as `app` for Vercel
app = application
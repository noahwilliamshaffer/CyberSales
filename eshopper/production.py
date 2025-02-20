import os
from .settings import *

DEBUG = False

# Configure allowed hosts for your Render.com domain
ALLOWED_HOSTS = ['.onrender.com', 'your-app-name.onrender.com']  # Replace with your actual domain

# Configure the database using the DATABASE_URL environment variable
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# Configure static files
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
] + MIDDLEWARE_CLASSES  # Note: Using MIDDLEWARE_CLASSES from your original settings

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Get secret key from environment variable
SECRET_KEY = os.environ.get('SECRET_KEY') 
import os

# Flask app settings
SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
MONGODB_HOST = os.environ.get('MONGODB_HOST') or 'mongodb'
MONGODB_PORT = int(os.environ.get('MONGODB_PORT') or 27017)

MONGODB_USERNAME = 'admin'
MONGODB_PASSWORD = 'admin'
MONGODB_DB = 'pyposterdb'

# MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME') or 'admin'
# MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD') or 'admin'
# MONGODB_DB = os.environ.get('MONGODB_DB') or 'pyposterdb'

# API key for movie poster images
API_KEY = 'MY TMDB API KEY'

# Flask-Bootstrap settings
BOOTSTRAP_SERVE_LOCAL = True

import os

# Flask app settings
SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
MONGODB_HOST = os.environ.get('MONGODB_HOST') or 'localhost'
MONGODB_PORT = int(os.environ.get('MONGODB_PORT') or 27017)
MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME') or 'my-mongo-user'
MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD') or 'my-mongo-password'
MONGODB_DB = os.environ.get('MONGODB_DB') or 'my-mongo-db'

# API key for movie poster images
API_KEY = 'MY TMDB API KEY'

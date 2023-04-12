# Set the environment variables for the Docker Compose file
import os

os.environ['MONGO_INITDB_ROOT_USERNAME'] = 'admin'
os.environ['MONGO_INITDB_ROOT_PASSWORD'] = 'password123'
os.environ['FLASK_ENV'] = 'development'
os.environ['API_KEY'] = 'MY TMDB API KEY'

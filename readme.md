# Movie API Project

This is a project that allows you to retrieve information about movies from an external API and store them in a MongoDB database.

## Getting Started
### virtual environment
To get started, clone this repository and navigate to the root directory. Then, create a virtual environment and activate it:

python -m venv env
source env/bin/activate

### Install Required Dependencies
Install the required dependencies by running:

pip install -r app/requirements.txt

### Edit config files
Edit the files:
docker-compose-config.py
app/app-config.py
db/db-config.py

To add your passwords and api key.

## Start the application
To start the application, run the following command from the root directory:

docker-compose up


## API Endpoints

### GET /movies

Retrieves a list of movies from the external API and returns them as JSON.

### GET /movies/{id}

Retrieves a single movie by its ID from the database and returns it as JSON.

### POST /movies

Adds a new movie to the database. The movie data should be sent in the request body as JSON.

## Docker

This project includes Docker containers for both the application and the database. To build and run the containers, use the following commands:

docker-compose build
docker-compose up

# New Instance
sudo apt-get update
sudo apt-get install git
https://github.com/michaelbenis/PyPoster
cd PyPoster
pip install Flask

docker run -e API_KEY=<YOUR_TMDB_API_KEY> -p 5000:5000 pyposter

# Movie API Project

This is a project that allows you to retrieve information about movies from an external API and store them in a MongoDB database.

## Getting Started

To get started, clone this repository and navigate to the root directory. Then, create a virtual environment and activate it:

python -m venv env
source env/bin/activate


Install the required dependencies by running:

pip install -r app/requirements.txt


Next, create a `config.py` file in the `app/` directory with the following content:

API_KEY = 'your_api_key_here'


Replace `your_api_key_here` with your actual API key.

Create a `db-config.py` file in the `db/` directory with the following content:

DB_HOST = 'mongodb://mongo:27017/'
DB_NAME = 'my-mongo-db'
DB_USERNAME = 'admin'
DB_PASSWORD = 'admin'


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


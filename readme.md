# PyPoster

PyPoster is a Python web application that allows users to search for movies and create posters for their favorite movies.

## Getting Started

These instructions will help you get a copy of the PyPoster project up and running on your local machine or on an EC2 instance.

### Prerequisites

Before you start, make sure you have the following installed on your machine:

- Git
- Docker

If you are using an EC2 instance, make sure it has at least 1GB of RAM.

### Installing Docker

If you don't already have Docker installed, you can install it by following the steps below:

1. Update the package index on your EC2 instance: `sudo apt-get update`

2. Install the latest version of Docker:

sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release

sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

sudo apt install docker-compose


3. Verify that Docker is installed correctly by running the following command:

sudo docker --version

### Setting up the PyPoster app

To set up the PyPoster app, follow the steps below:

1. Clone the PyPoster repository: 

git clone https://github.com/YOUR_USERNAME/PyPoster.git

3. Navigate to the project directory: `cd PyPoster`

4. Change the TMDB aPI Key in app/app-config.py 

API_KEY = 'MY TMDB API KEY'

5. Change the Database username and password in db/init-mongo.js

  user: "admin",
  pwd: "admin",

6. Build the app Docker image: 

cd app
sudo docker build -t pyposterapp .

7. Build the db Docker image: 

cd db
sudo docker build -t pyposterdb .


8. Run the Docker containers: 

docker-compose up

9. Open your web browser and go to `http://YOUR_EC2_INSTANCE_PUBLIC_IP_ADDRESS:5000` to access the PyPoster app.

## Built With

- Flask - A micro web framework written in Python
- MongoDB - A document-based, distributed database system
- Docker - A containerization platform

from flask import jsonify
from pymongo import MongoClient
from app import app


@app.route('/')
def index():
    client = MongoClient(
        host=app.config['MONGODB_HOST'],
        port=app.config['MONGODB_PORT'],
        username=app.config['MONGODB_USERNAME'],
        password=app.config['MONGODB_PASSWORD'],
        authSource=app.config['MONGODB_DB']
    )
    db = client[app.config['MONGODB_DB']]
    movies = db.movies.find()
    response = []
    for movie in movies:
        movie['_id'] = str(movie['_id'])
        response.append(movie)
    return jsonify(response)


if __name__ == '__main__':
    app.run()

import requests
import os
from config import api_key

def get_movie_id(title):
    """
    Given a movie title, return the movie's ID from TMDb API.

    Args:
        title (str): the title of the movie to search for.

    Returns:
        str: the ID of the first movie matching the search query.
    """
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": api_key,
        "query": title
    }
    response = requests.get(url, params=params)
    response_json = response.json()
    if response_json["total_results"] == 0:
        return None
    return str(response_json["results"][0]["id"])

def download_poster(movie_id):
    """
    Given a movie ID, download the movie poster and save it to the
    "posters" directory.

    Args:
        movie_id (str): the ID of the movie to download the poster for.

    Returns:
        str: the path to the downloaded poster file.
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    params = {
        "api_key": api_key
    }
    response = requests.get(url, params=params)
    response_json = response.json()
    if len(response_json["posters"]) == 0:
        return None
    poster_url = f"https://image.tmdb.org/t/p/w500/{response_json['posters'][0]['file_path']}"
    poster_path = os.path.join("posters", f"{movie_id}.jpg")
    if not os.path.exists(poster_path):
        response = requests.get(poster_url)
        with open(poster_path, "wb") as f:
            f.write(response.content)
    return poster_path

def show_poster(poster_path):
    """
    Given a path to a movie poster file, open and display the poster.

    Args:
        poster_path (str): the path to the movie poster file.
    """
    import platform
    if platform.system() == "Darwin":  # macOS
        os.system(f"open {poster_path}")
    elif platform.system() == "Windows":
        os.system(f'start "" "{poster_path}"')
    else:  # Linux or other
        os.system(f"xdg-open {poster_path}")

if __name__ == "__main__":
    movie_title = input("Enter movie title: ")
    movie_id = get_movie_id(movie_title)
    if movie_id is not None:
        poster_path = download_poster(movie_id)
        print("Poster downloaded successfully!")
        show_poster(poster_path)
    else:
        print("No movie found with that title.")

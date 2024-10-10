import os
from dotenv import load_dotenv
import tmdbsimple

# Load API key from environment variable
load_dotenv()
tmdbsimple.API_KEY = os.getenv('TMDB_API_KEY')


def get_tmdb_movie_details(title):
    """
    Fetches details about a movie from The Movie Database (TMDb) API.
    """
    try:
        search = tmdbsimple.Search()
        response = search.movie(query=title)
        if search.results:
            movie_id = search.results[0]['id']
            movie = tmdbsimple.Movies(movie_id)
            movie_info = movie.info()
            movie_details = {
                'title': movie_info.get('title'),
                'year': movie_info.get('release_date', '')[:4],
                'description': movie_info.get('overview'),
                'genre': [genre['name'] for genre in movie_info.get('genres', [])],
                'country_of_origin': [country['name'] for country in movie_info.get('production_countries', [])],
            }
            return movie_details
        else:
            return {'Error': 'Movie not found'}
    except Exception as e:
        print(f"Error fetching movie details: {e}")
        return {'Error': 'Failed to fetch movie details.'}



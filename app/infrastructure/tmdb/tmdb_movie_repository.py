from app.domain.models.movie import Movie
from app.domain.repositories.movie_repository import MovieRepository
from app.infrastructure.tmdb.tmdb_api_client import TMDBApiClient
from typing import List


class TmdbMovieRepository(MovieRepository):
    def __init__(self, tmdb_api_key: str):

        self.client = TMDBApiClient(tmdb_api_key)

    def search_movies(self, query: str) -> List[Movie]:
        response = self.client.search_movies(query)
        movies = [
            Movie(
                movie_id=movie["id"],
                title=movie["title"],
                release_date=movie["release_date"],
            )
            for movie in response["results"]
        ]
        return movies

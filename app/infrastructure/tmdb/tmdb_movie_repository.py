""" This module defines the TMDBMovieRepository class. """

from typing import List
from app.domain.models.movie import Movie
from app.domain.repositories.movie_repository import MovieRepository
from app.infrastructure.tmdb.tmdb_api_client import TMDBApiClient


class TmdbMovieRepository(MovieRepository):
    """
    Class for representing a movie repository using the TMDB API.
    """

    def __init__(self, tmdb_api_key: str):
        """Initialize the repository with the provided API key.

        Args:
            tmdb_api_key: The API key to use for authentication.
        """

        self.client = TMDBApiClient(tmdb_api_key)

    def search_movies(self, query: str) -> List[Movie]:
        """Search for movies using the TMDB API.

        Args:
            query: The query to search for.

        Returns:
            A list of movies matching the query.
        """
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

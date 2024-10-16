""" This module defines the SearchMovies class. """

from typing import List
from app.domain.models.movie import Movie
from app.domain.repositories.movie_repository import MovieRepository


class SearchMovies:
    """Class for searching for movies."""

    def __init__(self, movie_repository: MovieRepository):
        """Initialize the SearchMovies class.

        Args:
            movie_repository: The movie repository to use for searching.
        """
        self.movie_repository = movie_repository

    def execute(self, query: str) -> List[Movie]:
        """Searches for movies in the repository with the given query.

        Args:
            query: The query to search for.

        Returns:
            A list of movies matching the query.
        """
        return self.movie_repository.search_movies(query)

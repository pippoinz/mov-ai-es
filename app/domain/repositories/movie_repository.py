"""This module defines the MovieRepository interface."""

from typing import List
from abc import ABC, abstractmethod
from app.domain.models.movie import Movie


class MovieRepository(ABC):
    """Class for representing a movie repository."""

    @abstractmethod
    def search_movies(self, query: str) -> List[Movie]:
        """Searches for movies in the repository with the given query.

        Args:
            query: The query to search for.

        Returns:
            A list of movies matching the query.
        """

from app.domain.models.movie import Movie
from app.domain.repositories.movie_repository import MovieRepository
from typing import List


class SearchMovies:
    def __init__(self, movie_repository: MovieRepository):
        self.movie_repository = movie_repository

    def execute(self, query: str) -> List[Movie]:
        return self.movie_repository.search_movies(query)

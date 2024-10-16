from typing import List
from abc import ABC, abstractmethod
from app.domain.models.movie import Movie


class MovieRepository(ABC):
    @abstractmethod
    def search_movies(self, query: str) -> List[Movie]:
        pass

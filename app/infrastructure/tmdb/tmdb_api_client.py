import requests
from requests.exceptions import HTTPError

from config import settings


class TMDBApiClient:
    def __init__(self, api_key: str):

        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"

    def _make_request(self, endpoint: str, params: dict):
        """Generate a request to the TMDB API."""
        url = f"{self.base_url}/{endpoint}"
        params["api_key"] = self.api_key
        params["language"] = settings.TMDB_LANGUAGE

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
        except HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")

        return response.json()

    def search_movies(self, query: str):
        """Search for movies using the TMDB API."""
        endpoint = "search/movie"
        params = {"query": query}
        return self._make_request(endpoint, params)

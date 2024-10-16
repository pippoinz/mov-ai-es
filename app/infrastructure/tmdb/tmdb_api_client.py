""" This module contains the TMDB API client. """

import requests

from config import settings


class TMDBApiClient:
    """
    Class for interacting with the TMDB API.
    """

    def __init__(self, api_key: str):
        """Initialize the client with the provided API key.

        Args:
            api_key: The API key to use for authentication.
        """
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"

    def _make_request(self, endpoint: str, params: dict):
        """Generate a request to the TMDB API.

        Args:
            endpoint: The endpoint to make the request to.
            params: The parameters to include in the request.

        Returns:
            The response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        params["api_key"] = self.api_key
        params["language"] = settings.TMDB_LANGUAGE

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors

        return response.json()

    def search_movies(self, query: str):
        """Search for movies using the TMDB API."""
        endpoint = "search/movie"
        params = {"query": query}
        return self._make_request(endpoint, params)

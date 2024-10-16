"""This module defines the Movie model."""


class Movie:
    """Class for representing a movie."""

    def __init__(self, movie_id, title, release_date):
        self.movie_id = movie_id
        self.title = title
        self.release_date = release_date

    def __str__(self):
        return f"Movie(id={self.movie_id}, title={self.title}, release_date={self.release_date})"

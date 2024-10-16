import sys

from config import settings
from app.application.use_cases.search_movies import SearchMovies
from app.infrastructure.tmdb.tmdb_movie_repository import TmdbMovieRepository


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <movie_name>")
        sys.exit(1)

    api_key = settings.TMDB_API_KEY
    movie_repository = TmdbMovieRepository(api_key)
    search_movies = SearchMovies(movie_repository)

    query = " ".join(sys.argv[1:])

    try:
        movies = search_movies.execute(query)
        if movies:
            for movie in movies:
                print(movie)
        else:
            print("No movies found for the given query.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

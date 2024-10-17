""" This module contains the settings for the application. """

import os
import locale
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

if not TMDB_API_KEY:
    raise ValueError("TMDB_API_KEY is missing from .env file")

# Language
TMDB_LANGUAGE = os.getenv(
    "TMDB_LANGUAGE", locale.getdefaultlocale()[0].replace("_", "-")
)

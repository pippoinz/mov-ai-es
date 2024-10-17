
# Mov.ai.es

[![Python application](https://github.com/pippoinz/mov-ai-es/actions/workflows/python-app.yml/badge.svg)](https://github.com/pippoinz/mov-ai-es/actions/workflows/python-app.yml)

[![codecov](https://codecov.io/gh/pippoinz/mov-ai-es/graph/badge.svg?token=FMU9DIBW6X)](https://codecov.io/gh/pippoinz/mov-ai-es)

**Description**: An application for movies, made more powerful by AI.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Environment Setup](#environment-setup)
  - [API Keys](#api-keys)
  - [Dependencies](#dependencies)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Mov.ai.es is an application designed to search, view, and analyze movie data with the enhanced power of artificial intelligence. The application integrates movie data from the TMDB API and generates summaries, recommendations, and insights using the OpenAI API.

## Project Structure
```text
project_root/
|-- app/
|   |-- domain/
|   |-- application/
|   |-- infrastructure/
|   |-- interface/
|-- config/
|-- tests/
|-- README.md
|-- requirements.txt
```

## Setup Instructions

### Environment Setup
To set up the environment, ensure you have the following:
- Python 3.x installed
- Virtual environment (optional but recommended)

You can create a virtual environment and install dependencies using:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### API Keys
You'll need API keys for the following services:
- **TMDB API**: Create an account on [The Movie Database](https://www.themoviedb.org/) and get an API key.
- **OpenAI API**: Create an account on [OpenAI](https://beta.openai.com/) and get an API key.

Store these keys in a `.env` file:

```bash
TMDB_API_KEY=your_tmdb_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

### Dependencies
All required dependencies can be found in the `requirements.txt` file. You can install them with the following command:

```bash
pip install -r requirements.txt
```

## Running the Application

TODO

## Usage

TODO

## Contributing

If you want to contribute to the project, feel free to fork the repository and create pull requests. Be sure to follow the clean architecture structure when adding new features or fixing bugs.

## License

This project is licensed under the GNU General Public License v3.0 (GPL 3.0).

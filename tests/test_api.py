import pytest
from api.kinopoisk_api import KinopoiskAPI
from config.data import SEARCH_QUERY


@pytest.mark.api
def test_search_movie_status():
    api = KinopoiskAPI()
    response = api.search_movie(SEARCH_QUERY)
    assert response.status_code == 200


@pytest.mark.api
def test_search_movie_not_empty():
    api = KinopoiskAPI()
    response = api.search_movie(SEARCH_QUERY)
    data = response.json()
    assert data["films"]


@pytest.mark.api
def test_search_invalid_query():
    api = KinopoiskAPI()
    response = api.search_movie("asdkjasdhkashdk")
    data = response.json()
    assert len(data["films"]) == 0


@pytest.mark.api
def test_top_movies_status():
    api = KinopoiskAPI()
    response = api.get_top_movies()
    assert response.status_code == 200


@pytest.mark.api
def test_top_movies_structure():
    api = KinopoiskAPI()
    response = api.get_top_movies()
    data = response.json()
    assert "films" in data or "items" in data

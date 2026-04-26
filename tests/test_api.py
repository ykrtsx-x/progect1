import pytest
import allure
from api.kinopoisk_api import KinopoiskAPI
from config.data import SEARCH_QUERY


@pytest.mark.api
def test_search_movie_status():
    api = KinopoiskAPI()

    with allure.step("Отправить запрос поиска фильма"):
        response = api.search_movie(SEARCH_QUERY)

    with allure.step("Проверить статус код"):
        assert response.status_code == 200


@pytest.mark.api
def test_search_movie_not_empty():
    api = KinopoiskAPI()

    with allure.step("Отправить запрос поиска фильма"):
        response = api.search_movie(SEARCH_QUERY)
        data = response.json()

    with allure.step("Проверить, что список фильмов не пустой"):
        assert data["films"]


@pytest.mark.api
def test_search_invalid_query():
    api = KinopoiskAPI()

    with allure.step("Отправить невалидный запрос"):
        response = api.search_movie("asdkjasdhkashdk")
        data = response.json()

    with allure.step("Проверить, что результатов нет"):
        assert len(data["films"]) == 0


@pytest.mark.api
def test_top_movies_status():
    api = KinopoiskAPI()

    with allure.step("Получить топ фильмов"):
        response = api.get_top_movies()

    with allure.step("Проверить статус код"):
        assert response.status_code == 200


@pytest.mark.api
def test_top_movies_structure():
    api = KinopoiskAPI()

    with allure.step("Получить топ фильмов"):
        response = api.get_top_movies()
        data = response.json()

    with allure.step("Проверить структуру ответа"):
        assert "films" in data or "items" in data

import pytest
import allure
from pages.main_page import MainPage
from config.settings import BASE_URL


@pytest.mark.ui
def test_open_main_page(driver):
    page = MainPage(driver)

    with allure.step("Открыть главную страницу"):
        page.open(BASE_URL)

    with allure.step("Проверить заголовок страницы"):
        assert "Кинопоиск" in page.get_title()

    with allure.step("Проверить URL сайта"):
        assert "kinopoisk" in driver.current_url


@pytest.mark.ui
def test_search_movie(driver):
    page = MainPage(driver)

    with allure.step("Открыть главную страницу"):
        page.open(BASE_URL)

    with allure.step("Выполнить поиск фильма"):
        page.search("Интерстеллар")
        page.wait_for_search()

    with allure.step("Проверить, что открылась страница поиска"):
        assert "kp_query" in driver.current_url


@pytest.mark.ui
def test_go_to_movies(driver):
    page = MainPage(driver)

    with allure.step("Открыть главную страницу"):
        page.open(BASE_URL)

    with allure.step("Перейти в раздел фильмов"):
        page.go_to_movies()

    with allure.step("Проверить, что произошёл переход"):
        assert driver.current_url != BASE_URL


@pytest.mark.ui
def test_go_to_series(driver):
    page = MainPage(driver)

    with allure.step("Открыть главную страницу"):
        page.open(BASE_URL)

    with allure.step("Перейти в раздел сериалов"):
        page.go_to_series()

    with allure.step("Проверить, что произошёл переход"):
        assert driver.current_url != BASE_URL


@pytest.mark.ui
def test_page_title_not_empty(driver):
    page = MainPage(driver)

    with allure.step("Открыть главную страницу"):
        page.open(BASE_URL)

    with allure.step("Проверить, что заголовок не пустой"):
        assert page.get_title() != ""

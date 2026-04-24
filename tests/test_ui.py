
import pytest
from pages.main_page import MainPage
from config.settings import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.ui
def test_open_main_page(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    assert "Кинопоиск" in page.get_title()


@pytest.mark.ui
def test_search_movie(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    page.search("Интерстеллар")

    WebDriverWait(driver, 10).until(
        EC.url_contains("kp_query")
    )

    assert "kp_query" in driver.current_url


@pytest.mark.ui
def test_search_empty(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    page.search("")
    assert "kinopoisk" in driver.current_url.lower()


@pytest.mark.ui
def test_page_title_not_empty(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    assert page.get_title() != ""


@pytest.mark.ui
def test_url_contains_domain(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    assert "kinopoisk" in driver.current_url

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainPage:

    SEARCH_INPUT = (By.NAME, "kp_query")

    MOVIES = (By.LINK_TEXT, "Фильмы")
    SERIES = (By.LINK_TEXT, "Сериалы")
    TICKETS = (By.LINK_TEXT, "Билеты")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def search(self, text):
        input_field = self.driver.find_element(*self.SEARCH_INPUT)
        input_field.clear()
        input_field.send_keys(text)
        input_field.send_keys(Keys.ENTER)

    def wait_for_search(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("kp_query")
        )

    def wait_for_url_contains(self, text):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        WebDriverWait(self.driver, 10).until(
            EC.url_contains(text)
        )

    def go_to_movies(self):
        self.driver.find_element(*self.MOVIES).click()

    def go_to_series(self):
        self.driver.find_element(*self.SERIES).click()

    def go_to_tickets(self):
        self.driver.find_element(*self.TICKETS).click()

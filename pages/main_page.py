from selenium.webdriver.common.by import By


class MainPage:

    SEARCH_INPUT = (By.NAME, "kp_query")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def search(self, text):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(text)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def get_title(self):
        return self.driver.title

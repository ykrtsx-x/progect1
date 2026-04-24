import requests
from config.settings import API_URL
from config.data import API_KEY


class KinopoiskAPI:

    def __init__(self):
        self.headers = {
            "X-API-KEY": API_KEY
        }

    def search_movie(self, query):
        return requests.get(
            f"{API_URL}/v2.1/films/search-by-keyword",
            headers=self.headers,
            params={"keyword": query}
        )

    def get_top_movies(self):
        return requests.get(
            f"{API_URL}/v2.2/films/top",
            headers=self.headers
        )

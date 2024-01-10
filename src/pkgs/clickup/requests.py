from .config import ClickupConfig
from .list import List


class Requests:
    def __init__(self):
        self.__config = ClickupConfig()
        self.__gdps = self.__config.gdps

    @property
    def gdps(self) -> list:
        return self.__gdps

    @property
    def list(self):
        return List(url_base=self.__config.url_base, api_token=self.__config.api_token)

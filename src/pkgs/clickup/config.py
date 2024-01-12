import json
from typing import List


class ClickupConfig:
    def __init__(self):
        with open('config.json', 'r') as config_file:
            self.__config: dict = json.load(config_file)

    @property
    def api_token(self) -> str:
        return self.__config['api_token']

    @property
    def url_base(self) -> str:
        return self.__config['url_base']

    @property
    def gdps(self) -> List[int]:
        gdps: dict = self.__config['gdps']
        return [gdp for gdp in gdps.values()]

    @property
    def subtasks(self) -> bool:
        return self.__config['subtasks']

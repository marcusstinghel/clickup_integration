import logging as log
from src.config import Env, Log
from src.pkgs.clickup import Requests, Task
from src.pkgs.csv import File


class ClickupCards2Csv:

    def __init__(self):
        Log.configurator()
        self.__env_config = Env()
        self.__requests = Requests()

    def run(self) -> None:
        log.info('Iníciando execução')
        csv_file = File(path='csv/data.csv')
        all_cards: int = 0
        for gdp in self.__requests.gdps:
            log.info(f'gdp: {gdp}')
            cards_per_request: int = 100
            page: int = 0
            while cards_per_request >= 100:
                cards: list[Task] = self.__requests.list.get(list_id=gdp, page=page).tasks
                log.info(f'page: {page}, quantidade: {len(cards)}')
                csv_file.insert_cards_pack(cards=cards)
                cards_per_request = len(cards)
                all_cards += cards_per_request
                page += 1
        log.info(f'quantidade de cards total: {all_cards}')

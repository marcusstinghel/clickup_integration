import logging as log
from src.config import Env, Log
from src.pkgs.clickup import Requests


class ClickupCards2Consinco:

    def __init__(self):
        Log.configurator()
        self.__env_config = Env()
        self.__requests = Requests()

    def run(self) -> None:
        cards: list = self.__get_cards()
        self.__csv_inserter(cards=cards)

    def __csv_inserter(self, cards: list) -> None:
        pass

    def __get_cards(self) -> list:
        all_cards: list = []
        for gdp in self.__requests.gdps:
            minimum_cards_per_request: int = 1
            page: int = 0
            log.info(f'gdp: {gdp}')
            while minimum_cards_per_request > 0:
                request_cards = self.__requests.list.get(list_id=gdp, page=page)
                minimum_cards_per_request = len(request_cards.tasks)
                all_cards.extend(card for card in request_cards.tasks)
                log.info(f'page: {page}, quantidade: {minimum_cards_per_request}')
                page += 1
        log.info(f'quantidade de cards total: {len(all_cards)}')
        return all_cards

import requests
from .models import RequestGet, ResponseGet


class ListRequests:
    def __init__(self, basic_config: dict):
        self.__basic_config = basic_config

    def get(self, list_id: int, page: int) -> ResponseGet:
        request_model = RequestGet(basic_config=self.__basic_config, list_id=list_id, page=page)
        response = requests.get(url=request_model.url, headers=request_model.header)
        return ResponseGet(**response.json())

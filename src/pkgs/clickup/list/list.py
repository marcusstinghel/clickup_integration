import requests
from .models import RequestGet, ResponseGet


class List:
    def __init__(self, url_base: str, api_token: str):
        self.__url_base = url_base
        self.__api_token = api_token

    def get(self, list_id: int, page: int) -> ResponseGet:
        request_model = RequestGet(
            url_base=self.__url_base,
            api_token=self.__api_token,
            list_id=list_id,
            page=page
        )
        response = requests.get(url=request_model.url, headers=request_model.header, params=request_model.params)
        return ResponseGet(**response.json())

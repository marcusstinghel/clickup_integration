class RequestGet:
    def __init__(self, basic_config: dict, list_id: int, page: int = 0) -> None:
        self.__url_base = basic_config['url_base']
        self.__auth = basic_config['token_api']
        self.__list_id = list_id
        self.__page = page

    @property
    def url(self) -> str:
        return f'{self.__url_base}list/{self.__list_id}/task?page={self.__page}&include_closed=true'

    @property
    def header(self) -> dict:
        return {'Authorization': self.__auth}

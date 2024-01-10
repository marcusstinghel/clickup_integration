class RequestGet:
    def __init__(self, url_base: str, api_token: str, list_id: int, page: int = 0) -> None:
        self.__url_base = url_base
        self.__auth = api_token
        self.__list_id = list_id
        self.__page = page

    @property
    def url(self) -> str:
        return f'{self.__url_base}/list/{self.__list_id}/task'

    @property
    def header(self) -> dict:
        return {'Authorization': self.__auth}

    @property
    def params(self) -> dict:
        return {'page': {self.__page}, 'include_closed': 'true', 'subtasks': 'true'}

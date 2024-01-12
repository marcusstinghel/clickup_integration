class RequestGet:
    def __init__(self, url_base: str, api_token: str, subtasks: bool, list_id: int, page: int = 0) -> None:
        self.__url_base = url_base
        self.__auth = api_token
        self.__subtasks = subtasks
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
        params = {'page': self.__page, 'include_closed': 'true'}
        if self.__subtasks:
            params['subtasks'] = 'true'
        return params

class HttpClient:
    def __init__(self, url: str, headers: dict[str, str]):
        self._url: str = url
        self._headers: dict[str, str] = headers

    def add(self, obj: dict) -> None:
        print(f'America client: {obj}')

    def update(self, obj: dict) -> None:
        print(f'America client: {obj}')

    def delete(self, obj: dict) -> None:
        print(f'America client: {obj}')
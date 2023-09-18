import httpx


class HttpClient:
    def __init__(self, url: str, headers: dict[str, str] | None = None):
        # not closing the connection because america-k8s-collector suppose to run indefinitely
        # and potentially a lot of resources will be changed frequently in heavy-loaded cluster
        self._client = httpx.Client(headers=headers)
        self._url: str = url
        self._headers: dict[str, str] = headers

    def add(self, obj: dict) -> None:
        print(f'HTTP client add: {obj}')
        self._client.post(self._url, json=obj)
        print(f'HTTP client added: {obj}')

    def update(self, obj: dict) -> None:
        print(f'HTTP client update: {obj}')
        self._client.put(self._url, json=obj)
        print(f'HTTP client updated: {obj}')

    def delete(self, obj: dict) -> None:
        print(f'HTTP client delete: {obj}')
        # using request because delete doesn't support body, the receiver must not ignore body on delete
        self._client.request("DELETE", self._url, json=obj)
        print(f'HTTP client deleted: {obj}')

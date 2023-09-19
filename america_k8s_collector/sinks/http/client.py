import httpx


class HttpClient:
    def __init__(self, url: str, headers: dict[str, str] | None = None):
        # not closing the connection because america-k8s-collector suppose to run indefinitely
        # and potentially a lot of resources will be changed frequently in heavy-loaded cluster
        self._client = httpx.Client(headers=headers)
        self._url: str = url
        self._headers: dict[str, str] = headers

    def add(self, obj: dict) -> None:
        self._client.post(self._url, json=obj)

    def update(self, obj: dict) -> None:
        self._client.put(self._url, json=obj)

    def delete(self, obj: dict) -> None:
        # using request because delete doesn't support body, the receiver must not ignore body on delete
        self._client.request("DELETE", self._url, json=obj)

import httpx

from america_k8s_collector.sinks.http.headers_parsers.headers_parser import HttpSinkHeadersParser


class HttpClient:
    def __init__(self, url: str, headers: dict[str, str] | None, headers_parser: HttpSinkHeadersParser):
        # not closing the connection because america-k8s-collector suppose to run indefinitely
        # and potentially a lot of resources will be changed frequently in heavy-loaded cluster
        self._headers_parser: HttpSinkHeadersParser = headers_parser
        self._url: str = url
        self._preparsed_headers: dict[str, str] | None = headers
        self._parsed_headers: dict[str, str] | None = self._headers_parser.parse_headers(headers)
        self._client = httpx.Client(headers=self._parsed_headers)

    def add(self, obj: dict) -> None:
        self._client.post(self._url, json=obj)

    def update(self, obj: dict) -> None:
        self._client.put(self._url, json=obj)

    def delete(self, obj: dict) -> None:
        # using request because delete doesn't support body, the receiver must not ignore body on delete
        self._client.request("DELETE", self._url, json=obj)

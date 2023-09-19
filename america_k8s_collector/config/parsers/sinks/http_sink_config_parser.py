from america_k8s_collector.config.models.sinks import SinkConfig
from america_k8s_collector.config.models.sinks.http import HttpSinkConfig, Header
from america_k8s_collector.config.parsers.exceptions import ParseError
from america_k8s_collector.config.parsers.sinks.sink_parser import SinkConfigParser


class HttpSinkConfigParser(SinkConfigParser):
    def parse(self, sink_obj: dict) -> SinkConfig:
        sink_type: str = sink_obj['type']
        url: str = sink_obj['url']
        headers: list[Header] | None = self._parse_headers(sink_obj)
        return HttpSinkConfig(type=sink_type, url=url, headers=headers)

    def _parse_headers(self, sink_obj: dict) -> list[Header] | None:
        headers: list[dict[str, str]] | None = sink_obj.get('headers')
        if not headers:
            return None
        try:
            return [Header(key=header['key'], value=header['value']) for header in headers]
        except KeyError as err:
            raise ParseError(f"Couldn't find {err} in sink config")

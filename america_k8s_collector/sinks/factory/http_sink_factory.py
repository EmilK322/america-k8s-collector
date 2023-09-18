from america_k8s_collector.config.models import Resource
from america_k8s_collector.config.models.sinks.http import HttpSinkConfig
from america_k8s_collector.sinks import Sink
from america_k8s_collector.sinks.factory import SinkFactory
from america_k8s_collector.sinks.http import HttpSink
from america_k8s_collector.sinks.http.client import HttpClient


class HttpSinkFactory(SinkFactory):
    def get_sink(self, resource: Resource) -> Sink:
        self._raise_for_type(resource.sink, expected_type='http')
        # it's probably safe to assume the SinkConfig type is already validated and parsed to the specific type
        http_client: HttpClient = self._create_http_client(resource.sink)
        return HttpSink(http_client)

    def _create_http_client(self, sink: HttpSinkConfig) -> HttpClient:
        headers: dict[str, str] | None = self._convert_header_configs_to_headers(sink)
        return HttpClient(url=sink.url, headers=headers)

    def _convert_header_configs_to_headers(self, sink: HttpSinkConfig) -> dict[str, str] | None:
        if not sink.headers:
            return None

        return {header_config.key: header_config.value for header_config in sink.headers}

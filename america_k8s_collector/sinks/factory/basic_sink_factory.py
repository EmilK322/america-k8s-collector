from america_k8s_collector.config.models import Resource
from america_k8s_collector.sinks import Sink
from america_k8s_collector.sinks.factory.http_sink_factory import HttpSinkFactory
from america_k8s_collector.sinks.factory.sink_factory import SinkFactory


class BasicSinkFactory(SinkFactory):
    def __init__(self):
        self._sink_type_to_sink_factory_map: dict[str, SinkFactory] = {
            'http': HttpSinkFactory()
        }

    def get_sink(self, resource: Resource) -> Sink:
        return self._sink_type_to_sink_factory_map[resource.sink.type].get_sink(resource)

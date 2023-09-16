from config.models import Resource
from sinks import Sink
from sinks.factory.basic_sink_factory import BasicSinkFactory
from sinks.factory.sink_factory import SinkFactory


class SharedSinkFactory(SinkFactory):
    """
    cache the given sink factory or BasicSinkFactory if not provided with id(Resource) as cache key
    """
    def __init__(self, sink_factory: SinkFactory | None = None):
        self._sink_factory: SinkFactory = sink_factory or BasicSinkFactory()
        self._shared_sinks: dict[int, Sink] = {}

    def get_sink(self, resource: Resource) -> Sink:
        # TODO: when sink property/list will be added to CollectorConfig we can cache based on sink properties and share it across resources
        resource_ref: int = id(resource)
        sink = self._shared_sinks.get(resource_ref)
        if not sink:
            sink = self._sink_factory.get_sink(resource)
            self._shared_sinks[resource_ref] = sink

        return sink

import abc

from america_k8s_collector.config.models import Resource
from america_k8s_collector.config.models.sinks import SinkConfig
from america_k8s_collector.sinks import Sink


class SinkFactory(abc.ABC):
    @abc.abstractmethod
    def get_sink(self, resource: Resource) -> Sink:
        raise NotImplementedError

    def _raise_for_type(self, sink: SinkConfig, expected_type: str) -> None:
        if sink.type != expected_type:
            raise ValueError(f'for {expected_type} sink use "type: {expected_type}", given type: {sink.type}')

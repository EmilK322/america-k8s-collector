import abc

from america_k8s_collector.config.models import Resource
from america_k8s_collector.sinks import Sink


class SinkFactory(abc.ABC):
    @abc.abstractmethod
    def get_sink(self, resource: Resource) -> Sink:
        raise NotImplementedError



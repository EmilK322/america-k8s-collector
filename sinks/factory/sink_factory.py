import abc

from config.models import Resource
from sinks import Sink


class SinkFactory(abc.ABC):
    @abc.abstractmethod
    def get_sink(self, resource: Resource) -> Sink:
        raise NotImplementedError



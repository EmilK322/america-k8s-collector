import abc

from america_k8s_collector.config.models import Resource


class EventProcessor(abc.ABC):
    @abc.abstractmethod
    def process(self, event: dict, resource: Resource) -> dict:
        raise NotImplementedError

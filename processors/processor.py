import abc

from config.models import Resource


class EventProcessor(abc.ABC):
    @abc.abstractmethod
    def process(self, event: dict, resource: Resource) -> dict:
        raise NotImplementedError

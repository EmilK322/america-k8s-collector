import abc

from config.models import CollectorConfig


class CollectorConfigParser(abc.ABC):

    @abc.abstractmethod
    def parse(self) -> CollectorConfig:
        raise NotImplementedError

import abc

from america_k8s_collector.config.models import CollectorConfig


class CollectorConfigParser(abc.ABC):

    @abc.abstractmethod
    def parse(self) -> CollectorConfig:
        raise NotImplementedError

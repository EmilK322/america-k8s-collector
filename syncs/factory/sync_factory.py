import abc

from config.models import Resource
from syncs import Sync


class SyncFactory(abc.ABC):
    @abc.abstractmethod
    def get_sync(self, resource: Resource) -> Sync:
        raise NotImplementedError



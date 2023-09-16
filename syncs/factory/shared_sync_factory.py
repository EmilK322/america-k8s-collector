from config.models import Resource
from syncs import Sync
from syncs.factory.basic_sync_factory import BasicSyncFactory
from syncs.factory.sync_factory import SyncFactory


class SharedSyncFactory(SyncFactory):
    """
    cache the given sync factory or BasicSyncFactory if not provided with id(Resource) as cache key
    """
    def __init__(self, sync_factory: SyncFactory | None = None):
        self._sync_factory: SyncFactory = sync_factory or BasicSyncFactory()
        self._shared_syncs: dict[int, Sync] = {}

    def get_sync(self, resource: Resource) -> Sync:
        # TODO: when sync property/list will be added to CollectorConfig we can cache based on sync properties and share it across resources
        resource_ref: int = id(resource)
        sync = self._shared_syncs.get(resource_ref)
        if not sync:
            sync = self._sync_factory.get_sync(resource)
            self._shared_syncs[resource_ref] = sync

        return sync

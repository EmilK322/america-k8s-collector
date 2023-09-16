from config.models import Resource
from syncs import Sync, AmericaSync
from syncs.america.client import AmericaClient
from syncs.factory.sync_factory import SyncFactory


class BasicSyncFactory(SyncFactory):
    # TODO: think about implement more syncs and add them to factory, maybe using some syntax in collector config
    def get_sync(self, resource: Resource) -> Sync:
        if not getattr(resource, 'sync', None):  # use the default sync, for Now its America
            return AmericaSync(AmericaClient('url', 'username', 'password'))

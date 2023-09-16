from syncs.america.client import AmericaClient
from syncs.sync import Sync


class AmericaSync(Sync):
    def __init__(self, america_client: AmericaClient):
        self._america_client = america_client

    def add(self, obj: dict) -> None:
        self._america_client.add(obj)

    def update(self, obj: dict) -> None:
        self._america_client.update(obj)

    def delete(self, obj: dict) -> None:
        self._america_client.delete(obj)

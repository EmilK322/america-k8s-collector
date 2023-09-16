from syncs.sync import Sync


class NOOPSync(Sync):
    def add(self, obj: dict) -> None:
        pass

    def update(self, obj: dict) -> None:
        pass

    def delete(self, obj: dict) -> None:
        pass

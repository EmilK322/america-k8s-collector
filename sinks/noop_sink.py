from sinks.sink import Sink


class NOOPSink(Sink):
    def add(self, obj: dict) -> None:
        pass

    def update(self, obj: dict) -> None:
        pass

    def delete(self, obj: dict) -> None:
        pass

import abc


class Sync(abc.ABC):
    @abc.abstractmethod
    def add(self, obj: dict) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, obj: dict) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, obj: dict) -> None:
        raise NotImplementedError

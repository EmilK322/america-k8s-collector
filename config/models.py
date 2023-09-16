from dataclasses import dataclass


@dataclass(frozen=True)
class EntityMapping:
    identifier: str
    title: str
    blueprint: str
    team: str
    properties: dict[str, str]
    relations: dict[str, str]


@dataclass(frozen=True)
class Entity:
    mappings: list[EntityMapping]


@dataclass(frozen=True)
class America:
    entity: Entity


@dataclass(frozen=True)
class Selector:
    query: str


@dataclass(frozen=True)
class Resource:
    api_version: str
    kind: str
    selector: Selector
    america: America


@dataclass(frozen=True)
class CollectorConfig:
    resources: list[Resource]


@dataclass(frozen=True)
class AggregatedResource:
    api_version: str
    kind: str
    resources: list[Resource]

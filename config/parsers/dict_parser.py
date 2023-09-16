from config.models import CollectorConfig, Resource, Selector, America, Entity, EntityMapping
from config.parsers.parser import CollectorConfigParser


class DictCollectorConfigParser(CollectorConfigParser):
    def __init__(self, obj: dict):
        self._obj = obj

    def parse(self) -> CollectorConfig:
        resources: list[dict] = self._obj['resources']
        resources: list[Resource] = [self._parse_resource(resource) for resource in resources]
        return CollectorConfig(resources=resources)

    def _parse_resource(self, resource: dict) -> Resource:
        api_version: str = resource['apiVersion']
        kind: str = resource['kind']
        selector: Selector = self._parse_selector(resource)
        america: America = self._parse_america(resource)
        return Resource(api_version=api_version, kind=kind, selector=selector, america=america)

    def _parse_selector(self, resource: dict) -> Selector:
        query: str = resource['selector']['query']
        return Selector(query=query)

    def _parse_america(self, resource: dict) -> America:
        mappings: list[dict] = resource['america']['entity']['mappings']
        entity_mappings: list[EntityMapping] = [self._parse_entity_mapping(mapping) for mapping in mappings]
        entity: Entity = Entity(mappings=entity_mappings)
        return America(entity=entity)

    def _parse_entity_mapping(self, mapping: dict) -> EntityMapping:
        return EntityMapping(identifier=mapping['identifier'],
                             title=mapping['title'],
                             blueprint=mapping['blueprint'],
                             team=mapping['team'],
                             properties=mapping['properties'],
                             relations=mapping.get('relations', {}))

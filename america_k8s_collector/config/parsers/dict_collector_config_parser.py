from america_k8s_collector.config.models import CollectorConfig, Resource, Selector, America, Entity, EntityMapping
from america_k8s_collector.config.models.sinks import SinkConfig
from america_k8s_collector.config.parsers.collector_config_parser import CollectorConfigParser
from america_k8s_collector.config.parsers.exceptions import ParseError
from america_k8s_collector.config.parsers.sinks.factory import SinkConfigParserFactory
from america_k8s_collector.config.parsers.sinks.sink_parser import SinkConfigParser


class DictCollectorConfigParser(CollectorConfigParser):
    def __init__(self, sink_config_parser_factory: SinkConfigParserFactory):
        self._sink_config_parser_factory = sink_config_parser_factory

    def parse(self, obj: dict) -> CollectorConfig:
        try:
            resources: list[dict] = obj['resources']
            resources: list[Resource] = [self._parse_resource(resource) for resource in resources]
            return CollectorConfig(resources=resources)
        except KeyError as err:
            raise ParseError(f"Couldn't find key {err} in config, check your config") from err

    def _parse_resource(self, resource: dict) -> Resource:
        api_version: str = resource['apiVersion']
        kind: str = resource['kind']
        selector: Selector = self._parse_selector(resource)
        america: America = self._parse_america(resource)
        sink_config: SinkConfig = self._parse_sink_config(resource)
        return Resource(api_version=api_version, kind=kind, selector=selector, america=america, sink=sink_config)

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
                             relations=mapping.get('relations'))

    def _parse_sink_config(self, resource: dict) -> SinkConfig:
        sink_obj: dict = resource['sink']
        sink_config_parser: SinkConfigParser = self._sink_config_parser_factory.get_sink_config_parser(sink_obj)
        return sink_config_parser.parse(sink_obj)

from dataclasses import asdict

from jmespath.parser import ParsedResult

from america_k8s_collector.config.models import Resource, EntityMapping
from america_k8s_collector.processors.processor import EventProcessor
from america_k8s_collector.utils.jmespath import JmesPathQueryCache


class JmesPathEventProcessor(EventProcessor):
    def __init__(self):
        self._resources_mapping_pair_to_query_cache: JmesPathQueryCache = JmesPathQueryCache()

    def process(self, event: dict, resource: Resource) -> dict:
        processed_mappings = []
        mappings: list[EntityMapping] = resource.america.entity.mappings
        for mapping in mappings:
            processed_mappings.append({
                'identifier': self._process_attribute(event, mapping.identifier),
                'title': self._process_attribute(event, mapping.title),
                'blueprint': self._process_attribute(event, mapping.blueprint),
                'team': self._process_attribute(event, mapping.team),
                'properties': self._process_properties(event, mapping.properties)
            })

        resource_dict: dict = asdict(resource)
        resource_dict['america']['entity']['mappings'] = processed_mappings
        return resource_dict

    def _process_properties(self, event: dict, properties: dict) -> dict:
        return {key: self._process_attribute(event, value) for key, value in properties.items()}

    def _process_attribute(self, event: dict, attribute: str) -> str:
        compiled_query: ParsedResult = self._resources_mapping_pair_to_query_cache.get_or_set(attribute)
        return compiled_query.search(event['raw_object'])

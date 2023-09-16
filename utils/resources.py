from collections import defaultdict

from config.models import Resource, CollectorConfig, AggregatedResource


def get_aggregated_resources(collector_config: CollectorConfig) -> list[AggregatedResource]:
    """
    get resources grouped by api_version and kind
    """
    aggregated_resources_map: dict[tuple[str, str], list[Resource]] = defaultdict(list)
    for resource in collector_config.resources:
        api_version_kind_pair: tuple[str, str] = resource.api_version, resource.kind
        aggregated_resources_map[api_version_kind_pair].append(resource)

    aggregated_resources: list[AggregatedResource] = [
        AggregatedResource(api_version=api_version, kind=kind, resources=resources)
        for (api_version, kind), resources
        in aggregated_resources_map.items()
    ]

    return aggregated_resources

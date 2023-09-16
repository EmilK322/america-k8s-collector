from time import sleep
from typing import NoReturn

from kubernetes import dynamic, config
from kubernetes.client import api_client

from config.models import AggregatedResource
from handlers import EventHandler
from listeners.resource_listener import ResourceListener


class BasicResourceListener(ResourceListener):
    def __init__(self, event_handler: EventHandler):
        self._event_handler: EventHandler = event_handler
        self._dynamic_client = dynamic.DynamicClient(
            api_client.ApiClient(configuration=config.load_kube_config())
        )
        self._resource_version: str = ''

    def listen(self, aggregated_resource: AggregatedResource) -> NoReturn:
        api: dynamic.Resource = self._dynamic_client.resources.get(api_version=aggregated_resource.api_version,
                                                                   kind=aggregated_resource.kind)

        while True:
            # TODO: change the namespace parameter or think about adding namespaces vs cluster features
            print(f'start listening to {api.api_version}/{api.kind}')
            for event in self._dynamic_client.watch(api, namespace='test', resource_version=self._resource_version):
                self._resource_version = self._get_next_resource_version(event)
                for resource in aggregated_resource.resources:
                    self._event_handler.handle(event, resource)

    def _get_next_resource_version(self, event: dict) -> str:
        next_resource_version = self._resource_version
        try:
            obj: dict = event["object"]
            metadata: dict | None = obj.get("metadata")
            if not metadata:
                print(f"Error getting getting metadata to get next resource version for event: {event}")
            else:
                next_resource_version = metadata["resourceVersion"]

        except Exception as err:
            print(f"Error getting next resource version for event: {event}, error: {err}")

        return next_resource_version

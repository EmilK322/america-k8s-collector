import traceback
from typing import Callable

from config.models import Resource
from filterers import EventFilterer
from handlers.event_handler import EventHandler
from processors import EventProcessor
from sinks import Sink
from sinks.factory import SinkFactory


class BasicEventHandler(EventHandler):
    def __init__(self, event_filterer: EventFilterer, event_processor: EventProcessor, sink_factory: SinkFactory):
        self._event_filterer: EventFilterer = event_filterer
        self._event_processor: EventProcessor = event_processor
        self._sink_factory = sink_factory
        self._event_type_to_handler_map: dict[str, Callable[[Sink, dict], None]] = {
            "ADDED": self._handle_added,
            "MODIFIED": self._handle_modified,
            "DELETED": self._handle_deleted,
        }

    def handle(self, event: dict, resource: Resource) -> None:
        event_type: str = event['type']
        event_raw_object: dict = event['raw_object']
        print(f'got event type: {event_type}')
        print(f'got raw object: {event_raw_object}')
        try:
            filtered_event: dict | None = self._event_filterer.filter(event, resource)
            if not filtered_event:
                print(f'filter out event')
                return
            processed_event: dict = self._event_processor.process(filtered_event, resource)
            sink: Sink = self._sink_factory.get_sink(resource)
            handler: Callable[[Sink, dict], None] | None = self._event_type_to_handler_map.get(event_type)
            if not handler:
                # TODO: define logging
                print(f'cannot handle event of type {event_type}, pass')
                return
            handler(sink, processed_event)
        except Exception as err:
            print(f'error occurred while handling event, error: {err}')
            traceback.print_exc()

    def _handle_added(self, sink: Sink, obj: dict) -> None:
        sink.add(obj)

    def _handle_modified(self, sink: Sink, obj: dict) -> None:
        sink.update(obj)

    def _handle_deleted(self, sink: Sink, obj: dict) -> None:
        sink.delete(obj)

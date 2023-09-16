from config.models import CollectorConfig, AggregatedResource
from config.parsers import YamlCollectorConfigParser
from filterers import JmesPathEventFilterer, EventFilterer
from handlers import BasicEventHandler, EventHandler
from listeners import ThreadedMultiResourceListener, BasicResourceListener, MultiResourceListener
from processors import JmesPathEventProcessor, EventProcessor
from syncs.factory import SharedSyncFactory, SyncFactory
from utils.resources import get_aggregated_resources

collector_config: CollectorConfig = YamlCollectorConfigParser(config_file_path='config.yaml').parse()
aggregated_resources: list[AggregatedResource] = get_aggregated_resources(collector_config)

sync_factory: SyncFactory = SharedSyncFactory()
event_filterer: EventFilterer = JmesPathEventFilterer()
event_processor: EventProcessor = JmesPathEventProcessor()
event_handler: EventHandler = BasicEventHandler(event_filterer, event_processor, sync_factory)
event_listener = BasicResourceListener(event_handler)
multi_resource_event_listener: MultiResourceListener = ThreadedMultiResourceListener(event_listener)

multi_resource_event_listener.listen(aggregated_resources)

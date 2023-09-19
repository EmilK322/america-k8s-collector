from america_k8s_collector.config.models import CollectorConfig, AggregatedResource
from america_k8s_collector.config.parsers import YamlCollectorConfigParser
from america_k8s_collector.config.parsers.sinks.factory import SinkConfigParserFactory, BasicSinkConfigParserFactory
from america_k8s_collector.filterers import JmesPathEventFilterer, EventFilterer
from america_k8s_collector.handlers import BasicEventHandler, EventHandler
from america_k8s_collector.listeners import ThreadedMultiResourceListener, BasicResourceListener, MultiResourceListener
from america_k8s_collector.processors import JmesPathEventProcessor, EventProcessor
from america_k8s_collector.sinks.factory import SharedSinkFactory, SinkFactory
from america_k8s_collector.utils.resources import get_aggregated_resources

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--namespace", type=str,
                    help="namespace to listen for resources, if not provided listen cluster-wide")
args = parser.parse_args()


sink_config_parser_factory: SinkConfigParserFactory = BasicSinkConfigParserFactory()
collector_config: CollectorConfig = YamlCollectorConfigParser(sink_config_parser_factory).parse_file('config.yaml')
aggregated_resources: list[AggregatedResource] = get_aggregated_resources(collector_config)

sink_factory: SinkFactory = SharedSinkFactory()
event_filterer: EventFilterer = JmesPathEventFilterer()
event_processor: EventProcessor = JmesPathEventProcessor()
event_handler: EventHandler = BasicEventHandler(event_filterer, event_processor, sink_factory)
event_listener = BasicResourceListener(event_handler)
multi_resource_event_listener: MultiResourceListener = ThreadedMultiResourceListener(event_listener)

multi_resource_event_listener.listen(aggregated_resources, args.namespace)

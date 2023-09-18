from america_k8s_collector.config.models import Resource
from america_k8s_collector.sinks import Sink, AmericaSink
from america_k8s_collector.sinks.america.client import AmericaClient
from america_k8s_collector.sinks.factory.sink_factory import SinkFactory


class BasicSinkFactory(SinkFactory):
    # TODO: think about implement more sinks and add them to factory, maybe using some syntax in collector config
    def get_sink(self, resource: Resource) -> Sink:
        if not getattr(resource, 'sink', None):  # use the default sink, for Now its America
            return AmericaSink(AmericaClient('url', 'username', 'password'))

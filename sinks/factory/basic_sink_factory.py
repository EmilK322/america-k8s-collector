from config.models import Resource
from sinks import Sink, AmericaSink
from sinks.america.client import AmericaClient
from sinks.factory.sink_factory import SinkFactory


class BasicSinkFactory(SinkFactory):
    # TODO: think about implement more sinks and add them to factory, maybe using some syntax in collector config
    def get_sink(self, resource: Resource) -> Sink:
        if not getattr(resource, 'sink', None):  # use the default sink, for Now its America
            return AmericaSink(AmericaClient('url', 'username', 'password'))

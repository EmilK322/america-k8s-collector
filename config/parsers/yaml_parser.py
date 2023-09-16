from pathlib import Path

import yaml

from config.models import CollectorConfig
from config.parsers.dict_parser import DictCollectorConfigParser
from config.parsers.parser import CollectorConfigParser


class YamlCollectorConfigParser(CollectorConfigParser):
    def __init__(self, config_file_path: str | Path):
        self._config_file_path = Path(config_file_path)
        with open(self._config_file_path, 'r') as file:
            self._collector_config = yaml.safe_load(file)
        self._dict_config_parser: DictCollectorConfigParser = DictCollectorConfigParser(self._collector_config)

    def parse(self) -> CollectorConfig:
        return self._dict_config_parser.parse()

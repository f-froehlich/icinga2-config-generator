import glob
from abc import abstractmethod

import pytest

from icinga2confgen.ConfigBuilder import ConfigBuilder


class BaseTest:

    @pytest.fixture(autouse=True)
    def configure(self):
        self._set_up()
        yield
        self._tear_down()
        ConfigBuilder.reset()

    def _set_up(self):
        pass

    def _tear_down(self):
        pass

    @abstractmethod
    def get_instance_class(self):
        raise NotImplementedError()

    def create_instance(self, force=False):
        return self.get_instance_class().create('instance', force_create=force)

    def test_config_files_placed_correctly(self, snapshot):
        self.create_instance()
        ConfigBuilder.get_config(True)
        config_files = glob.glob('zones.d/**/*.conf', recursive=True)

        for config_file in config_files:
            with open(config_file, 'r') as file:
                snapshot.assert_match(file.read(), config_file)

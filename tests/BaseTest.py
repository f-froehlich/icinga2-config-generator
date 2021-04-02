import glob
from abc import abstractmethod

import pytest
from pytest_snapshot.plugin import Snapshot, get_default_snapshot_dir

from icinga2confgen.ConfigBuilder import ConfigBuilder


class BaseTest:
    validate_snapshot = True

    @pytest.fixture(autouse=True)
    def configure(self, request):
        self.validate_snapshot = True
        self._set_up()
        try:
            yield

            if self.validate_snapshot:
                default_snapshot_dir = get_default_snapshot_dir(request.node)

                with Snapshot(request.config.option.snapshot_update,
                              request.config.option.allow_snapshot_deletion,
                              default_snapshot_dir) as snapshot:
                    snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'snapshot.txt')
        finally:
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

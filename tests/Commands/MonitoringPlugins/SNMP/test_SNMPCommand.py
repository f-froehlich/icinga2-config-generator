import pytest

from icinga2confgen.Commands.MonitoringPlugins.SNMP.SNMPCommand import SNMPCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder


class TestSNMPCommand:

    @pytest.fixture(autouse=True)
    def configure(self):
        yield
        ConfigBuilder.reset()

    def get_instance_class(self):
        return SNMPCommand

    def create_instance(self, force=False):
        instance = self.get_instance_class()('instance')
        ConfigBuilder.add_command('instance', instance)
        return instance

    def test_get_arguments_raise_exception(self):
        instance = self.create_instance()
        with pytest.raises(NotImplementedError) as excinfo:
            instance.get_arguments()

    def test_get_specific_arguments_raise_exception(self):
        instance = self.create_instance()
        with pytest.raises(NotImplementedError) as excinfo:
            instance.get_specific_arguments()

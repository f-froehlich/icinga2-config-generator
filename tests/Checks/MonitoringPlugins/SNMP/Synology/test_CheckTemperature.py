from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckTemperature import CheckTemperature
from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.TemperatureCommand import TemperatureCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckTemperature(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckTemperature

    def get_command_class(self):
        return TemperatureCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('synology'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

    def test_get_right_warning(self):
        instance = self.create_instance()
        instance.set_warning(44)

        assert 44 == instance.get_warning()

    def test_get_right_critical(self):
        instance = self.create_instance()
        instance.set_critical(55)

        assert 55 == instance.get_critical()

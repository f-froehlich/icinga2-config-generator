from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.TemperatureCommand import TemperatureCommand
from tests.BaseCommandTest import BaseCommandTest


class TestTemperatureCommand(BaseCommandTest):

    def get_instance_class(self):
        return TemperatureCommand

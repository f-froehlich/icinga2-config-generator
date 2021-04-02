from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.DiskTemperatureCommand import DiskTemperatureCommand
from tests.BaseCommandTest import BaseCommandTest


class TestDiskTemperatureCommand(BaseCommandTest):

    def get_instance_class(self):
        return DiskTemperatureCommand

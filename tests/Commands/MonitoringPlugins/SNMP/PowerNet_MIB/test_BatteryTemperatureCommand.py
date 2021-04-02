from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.BatteryTemperatureCommand import \
    BatteryTemperatureCommand
from tests.BaseCommandTest import BaseCommandTest


class TestBatteryTemperatureCommand(BaseCommandTest):

    def get_instance_class(self):
        return BatteryTemperatureCommand

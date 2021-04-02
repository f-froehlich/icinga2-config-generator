from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.BatteryStatusCommand import BatteryStatusCommand
from tests.BaseCommandTest import BaseCommandTest


class TestBatteryStatusCommand(BaseCommandTest):

    def get_instance_class(self):
        return BatteryStatusCommand

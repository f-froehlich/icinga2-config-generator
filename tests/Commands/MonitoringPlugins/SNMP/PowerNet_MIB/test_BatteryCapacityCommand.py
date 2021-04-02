from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.BatteryCapacityCommand import BatteryCapacityCommand
from tests.BaseCommandTest import BaseCommandTest


class TestBatteryCapacityCommand(BaseCommandTest):

    def get_instance_class(self):
        return BatteryCapacityCommand

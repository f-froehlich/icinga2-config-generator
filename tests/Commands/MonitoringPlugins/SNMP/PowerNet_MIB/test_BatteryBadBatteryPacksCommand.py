from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.BatteryBadBatteryPacksCommand import \
    BatteryBadBatteryPacksCommand
from tests.BaseCommandTest import BaseCommandTest


class TestBatteryBadBatteryPacksCommand(BaseCommandTest):

    def get_instance_class(self):
        return BatteryBadBatteryPacksCommand

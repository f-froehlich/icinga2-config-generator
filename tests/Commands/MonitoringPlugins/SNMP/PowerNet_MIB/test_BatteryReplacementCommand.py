from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.BatteryReplacementCommand import \
    BatteryReplacementCommand
from tests.BaseCommandTest import BaseCommandTest


class TestBatteryReplacementCommand(BaseCommandTest):

    def get_instance_class(self):
        return BatteryReplacementCommand

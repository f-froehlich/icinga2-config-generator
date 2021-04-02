from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.BatteryRemainingRuntimeCommand import \
    BatteryRemainingRuntimeCommand
from tests.BaseCommandTest import BaseCommandTest


class TestBatteryRemainingRuntimeCommand(BaseCommandTest):

    def get_instance_class(self):
        return BatteryRemainingRuntimeCommand

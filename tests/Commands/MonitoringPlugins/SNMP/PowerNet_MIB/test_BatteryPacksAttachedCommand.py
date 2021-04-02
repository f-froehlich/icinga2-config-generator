from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.BatteryPacksAttachedCommand import \
    BatteryPacksAttachedCommand
from tests.BaseCommandTest import BaseCommandTest


class TestBatteryPacksAttachedCommand(BaseCommandTest):

    def get_instance_class(self):
        return BatteryPacksAttachedCommand

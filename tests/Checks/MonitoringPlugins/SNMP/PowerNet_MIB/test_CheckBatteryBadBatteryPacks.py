from icinga2confgen.Checks.MonitoringPlugins.SNMP.PowerNet_MIB.CheckBatteryBadBatteryPacks import \
    CheckBatteryBadBatteryPacks
from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.BatteryBadBatteryPacksCommand import \
    BatteryBadBatteryPacksCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckBatteryBadBatteryPacks(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckBatteryBadBatteryPacks

    def get_command_class(self):
        return BatteryBadBatteryPacksCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ups'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

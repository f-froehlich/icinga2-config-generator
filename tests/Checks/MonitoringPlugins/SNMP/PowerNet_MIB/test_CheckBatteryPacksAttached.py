from icinga2confgen.Checks.MonitoringPlugins.SNMP.PowerNet_MIB.CheckBatteryPacksAttached import \
    CheckBatteryPacksAttached
from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.BatteryPacksAttachedCommand import \
    BatteryPacksAttachedCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckBatteryPacksAttached(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckBatteryPacksAttached

    def get_command_class(self):
        return BatteryPacksAttachedCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ups'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckSNMPTest.create_instance(self, force)
        instance.set_count(22)
        return instance

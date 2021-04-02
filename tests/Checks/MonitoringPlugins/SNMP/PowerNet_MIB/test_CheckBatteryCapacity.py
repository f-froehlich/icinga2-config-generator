from icinga2confgen.Checks.MonitoringPlugins.SNMP.PowerNet_MIB.CheckBatteryCapacity import CheckBatteryCapacity
from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.BatteryCapacityCommand import BatteryCapacityCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckBatteryCapacity(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckBatteryCapacity

    def get_command_class(self):
        return BatteryCapacityCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ups'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

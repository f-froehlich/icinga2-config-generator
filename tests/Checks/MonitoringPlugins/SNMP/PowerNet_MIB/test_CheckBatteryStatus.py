from icinga2confgen.Checks.MonitoringPlugins.SNMP.PowerNet_MIB.CheckBatteryStatus import CheckBatteryStatus
from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.BatteryStatusCommand import BatteryStatusCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckBatteryStatus(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckBatteryStatus

    def get_command_class(self):
        return BatteryStatusCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ups'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

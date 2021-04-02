from icinga2confgen.Checks.MonitoringPlugins.SNMP.PowerNet_MIB.CheckBatteryReplacement import CheckBatteryReplacement
from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.BatteryReplacementCommand import \
    BatteryReplacementCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckBatteryReplacement(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckBatteryReplacement

    def get_command_class(self):
        return BatteryReplacementCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ups'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

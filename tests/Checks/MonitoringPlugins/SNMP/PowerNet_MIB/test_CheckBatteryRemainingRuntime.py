from icinga2confgen.Checks.MonitoringPlugins.SNMP.PowerNet_MIB.CheckBatteryRemainingRuntime import \
    CheckBatteryRemainingRuntime
from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.BatteryRemainingRuntimeCommand import \
    BatteryRemainingRuntimeCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckBatteryRemainingRuntime(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckBatteryRemainingRuntime

    def get_command_class(self):
        return BatteryRemainingRuntimeCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ups'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

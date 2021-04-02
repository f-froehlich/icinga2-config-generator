from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckSystemStatus import CheckSystemStatus
from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.SystemStatusCommand import SystemStatusCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckSystemStatus(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckSystemStatus

    def get_command_class(self):
        return SystemStatusCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('synology'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

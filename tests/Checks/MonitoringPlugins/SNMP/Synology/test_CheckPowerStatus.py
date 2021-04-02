from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckPowerStatus import CheckPowerStatus
from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.PowerStatusCommand import PowerStatusCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckPowerStatus(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckPowerStatus

    def get_command_class(self):
        return PowerStatusCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('synology'),
            ServiceGroup.create('snmp')
        ]

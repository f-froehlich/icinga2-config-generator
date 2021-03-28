from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckCPUFanStatus import CheckCPUFanStatus
from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.CPUFanStatusCommand import CPUFanStatusCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest
from tests.BaseCheckTest import BaseCheckTest


class TestCheckCPUFanStatus(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckCPUFanStatus

    def get_command_class(self):
        return CPUFanStatusCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('synology'),
            ServiceGroup.create('snmp')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_username('user')
        instance.set_password('pwd')
        return instance

from icinga2confgen.Checks.MonitoringPlugins.CheckSPF import CheckSPF
from icinga2confgen.Commands.MonitoringPlugins.SPFCommand import SPFCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckSPF(BaseCheckTest):

    def get_instance_class(self):
        return CheckSPF

    def get_command_class(self):
        return SPFCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('spf'),
            ServiceGroup.create('dns'),
            ServiceGroup.create('security')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_expected('expected')
        instance.set_domain('domain')
        return instance

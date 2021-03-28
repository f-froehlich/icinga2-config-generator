from icinga2confgen.Checks.MonitoringPlugins.CheckOpenPorts import CheckOpenPorts
from icinga2confgen.Commands.MonitoringPlugins.OpenPortsCommand import OpenPortsCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckOpenPorts(BaseCheckTest):

    def get_instance_class(self):
        return CheckOpenPorts

    def get_command_class(self):
        return OpenPortsCommand

    def get_default_check_interval(self) -> str:
        return '24h'

    def get_default_check_timeout(self) -> int:
        return 12000

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('open_ports'),
            ServiceGroup.create('security'),
            ServiceGroup.create('nmap'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.add_host('host')
        return instance

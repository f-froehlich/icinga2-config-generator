from icinga2confgen.Checks.MonitoringPlugins.CheckCiphers import CheckCiphers
from icinga2confgen.Commands.MonitoringPlugins.CiphersCommand import CiphersCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckCiphers(BaseCheckTest):

    def get_instance_class(self):
        return CheckCiphers

    def get_command_class(self):
        return CiphersCommand

    def get_default_check_interval(self) -> str:
        return '24h'

    def get_default_check_timeout(self) -> int:
        return 12000

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ciphers'),
            ServiceGroup.create('nmap'),
            ServiceGroup.create('security'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.add_host('host')
        return instance

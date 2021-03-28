from icinga2confgen.Checks.MonitoringPlugins.CheckDenyTlsVersion import CheckDenyTlsVersion
from icinga2confgen.Commands.MonitoringPlugins.DenyTlsVersionCommand import DenyTlsVersionCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckDenyTlsVersion(BaseCheckTest):

    def get_instance_class(self):
        return CheckDenyTlsVersion

    def get_command_class(self):
        return DenyTlsVersionCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('webserver'),
            ServiceGroup.create('security'),
            ServiceGroup.create('tls'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_domain('host')
        instance.set_protocol('1.1')
        return instance

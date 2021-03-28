from icinga2confgen.Checks.MonitoringPlugins.CheckSSHDSecurity import CheckSSHDSecurity
from icinga2confgen.Commands.MonitoringPlugins.SSHDSecurityCommand import SSHDSecurityCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckSSHDSecurity(BaseCheckTest):

    def get_instance_class(self):
        return CheckSSHDSecurity

    def get_command_class(self):
        return SSHDSecurityCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('security'),
            ServiceGroup.create('sshd'),
            ServiceGroup.create('sshd_security'),
        ]

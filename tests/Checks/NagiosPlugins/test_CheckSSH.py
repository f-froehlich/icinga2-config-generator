from icinga2confgen.Checks.NagiosPlugins.CheckSSH import CheckSSH
from icinga2confgen.Commands.NagiosPlugins.SSHCommand import SSHCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckSSH(BaseCheckTest):

    def get_instance_class(self):
        return CheckSSH

    def get_command_class(self):
        return SSHCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('sshd')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_hostname('host')
        return instance

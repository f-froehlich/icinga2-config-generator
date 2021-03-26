from icinga2confgen.Commands.MonitoringPlugins.SSHDSecurityCommand import SSHDSecurityCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSSHDSecurityCommand(BaseCommandTest):

    def get_instance_class(self):
        return SSHDSecurityCommand

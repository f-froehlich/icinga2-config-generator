from icinga2confgen.Commands.NagiosPlugins.SSHCommand import SSHCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSSHCommand(BaseCommandTest):

    def get_instance_class(self):
        return SSHCommand

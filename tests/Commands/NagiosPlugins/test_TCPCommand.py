from icinga2confgen.Commands.NagiosPlugins.TCPCommand import TCPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestTCPCommand(BaseCommandTest):

    def get_instance_class(self):
        return TCPCommand

from icinga2confgen.Commands.NagiosPlugins.UDPCommand import UDPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestUDPCommand(BaseCommandTest):

    def get_instance_class(self):
        return UDPCommand

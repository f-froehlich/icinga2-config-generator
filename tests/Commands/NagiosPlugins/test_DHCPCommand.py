from icinga2confgen.Commands.NagiosPlugins.DHCPCommand import DHCPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestDHCPCommand(BaseCommandTest):

    def get_instance_class(self):
        return DHCPCommand

from icinga2confgen.Commands.NagiosPlugins.SNMPCommand import SNMPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSNMPCommand(BaseCommandTest):

    def get_instance_class(self):
        return SNMPCommand

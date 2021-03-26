from icinga2confgen.Commands.NagiosPlugins.SPOPCommand import SPOPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSPOPCommand(BaseCommandTest):

    def get_instance_class(self):
        return SPOPCommand

from icinga2confgen.Commands.NagiosPlugins.SIMAPCommand import SIMAPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSIMAPCommand(BaseCommandTest):

    def get_instance_class(self):
        return SIMAPCommand

from icinga2confgen.Commands.NagiosPlugins.SWAPCommand import SWAPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSWAPCommand(BaseCommandTest):

    def get_instance_class(self):
        return SWAPCommand

from icinga2confgen.Commands.NagiosPlugins.NTPTimeCommand import NTPTimeCommand
from tests.BaseCommandTest import BaseCommandTest


class TestNTPTimeCommand(BaseCommandTest):

    def get_instance_class(self):
        return NTPTimeCommand

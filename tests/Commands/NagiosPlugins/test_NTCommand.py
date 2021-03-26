from icinga2confgen.Commands.NagiosPlugins.NTCommand import NTCommand
from tests.BaseCommandTest import BaseCommandTest


class TestNTCommand(BaseCommandTest):

    def get_instance_class(self):
        return NTCommand

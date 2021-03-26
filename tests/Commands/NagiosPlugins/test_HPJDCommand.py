from icinga2confgen.Commands.NagiosPlugins.HPJDCommand import HPJDCommand
from tests.BaseCommandTest import BaseCommandTest


class TestHPJDCommand(BaseCommandTest):

    def get_instance_class(self):
        return HPJDCommand

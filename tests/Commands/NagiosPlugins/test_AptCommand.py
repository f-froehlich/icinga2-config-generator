from icinga2confgen.Commands.NagiosPlugins.AptCommand import AptCommand
from tests.BaseCommandTest import BaseCommandTest


class TestAptCommand(BaseCommandTest):

    def get_instance_class(self):
        return AptCommand

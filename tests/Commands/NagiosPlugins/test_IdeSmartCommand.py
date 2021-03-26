from icinga2confgen.Commands.NagiosPlugins.IdeSmartCommand import IdeSmartCommand
from tests.BaseCommandTest import BaseCommandTest


class TestIdeSmartCommand(BaseCommandTest):

    def get_instance_class(self):
        return IdeSmartCommand

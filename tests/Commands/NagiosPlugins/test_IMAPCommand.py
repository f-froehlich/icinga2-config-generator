from icinga2confgen.Commands.NagiosPlugins.IMAPCommand import IMAPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestIMAPCommand(BaseCommandTest):

    def get_instance_class(self):
        return IMAPCommand

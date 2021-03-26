from icinga2confgen.Commands.NagiosPlugins.FTPCommand import FTPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestFTPCommand(BaseCommandTest):

    def get_instance_class(self):
        return FTPCommand

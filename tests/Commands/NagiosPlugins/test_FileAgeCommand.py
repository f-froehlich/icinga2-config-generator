from icinga2confgen.Commands.NagiosPlugins.FileAgeCommand import FileAgeCommand
from tests.BaseCommandTest import BaseCommandTest


class TestFileAgeCommand(BaseCommandTest):

    def get_instance_class(self):
        return FileAgeCommand

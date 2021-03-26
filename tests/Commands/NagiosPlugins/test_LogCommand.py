from icinga2confgen.Commands.NagiosPlugins.LogCommand import LogCommand
from tests.BaseCommandTest import BaseCommandTest


class TestLogCommand(BaseCommandTest):

    def get_instance_class(self):
        return LogCommand

from icinga2confgen.Commands.NagiosPlugins.PingCommand import PingCommand
from tests.BaseCommandTest import BaseCommandTest


class TestPingCommand(BaseCommandTest):

    def get_instance_class(self):
        return PingCommand

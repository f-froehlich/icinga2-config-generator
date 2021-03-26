from icinga2confgen.Commands.NagiosPlugins.RPCCommand import RPCCommand
from tests.BaseCommandTest import BaseCommandTest


class TestRPCCommand(BaseCommandTest):

    def get_instance_class(self):
        return RPCCommand

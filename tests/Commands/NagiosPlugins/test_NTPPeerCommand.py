from icinga2confgen.Commands.NagiosPlugins.NTPPeerCommand import NTPPeerCommand
from tests.BaseCommandTest import BaseCommandTest


class TestNTPPeerCommand(BaseCommandTest):

    def get_instance_class(self):
        return NTPPeerCommand

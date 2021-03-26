from icinga2confgen.Commands.NagiosPlugins.ICMPCommand import ICMPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestICMPCommand(BaseCommandTest):

    def get_instance_class(self):
        return ICMPCommand

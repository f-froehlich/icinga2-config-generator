from icinga2confgen.Commands.NagiosPlugins.UptimeCommand import UptimeCommand
from tests.BaseCommandTest import BaseCommandTest


class TestUptimeCommand(BaseCommandTest):

    def get_instance_class(self):
        return UptimeCommand

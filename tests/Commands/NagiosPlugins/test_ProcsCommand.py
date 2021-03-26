from icinga2confgen.Commands.NagiosPlugins.ProcsCommand import ProcsCommand
from tests.BaseCommandTest import BaseCommandTest


class TestProcsCommand(BaseCommandTest):

    def get_instance_class(self):
        return ProcsCommand

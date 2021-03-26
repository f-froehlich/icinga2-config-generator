from icinga2confgen.Commands.NagiosPlugins.IfStatusCommand import IfStatusCommand
from tests.BaseCommandTest import BaseCommandTest


class TestIfStatusCommand(BaseCommandTest):

    def get_instance_class(self):
        return IfStatusCommand

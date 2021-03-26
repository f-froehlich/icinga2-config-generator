from icinga2confgen.Commands.NagiosPlugins.POPCommand import POPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestPOPCommand(BaseCommandTest):

    def get_instance_class(self):
        return POPCommand

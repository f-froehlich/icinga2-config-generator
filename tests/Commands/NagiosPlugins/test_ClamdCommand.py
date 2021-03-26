from icinga2confgen.Commands.NagiosPlugins.ClamdCommand import ClamdCommand
from tests.BaseCommandTest import BaseCommandTest


class TestClamdCommand(BaseCommandTest):

    def get_instance_class(self):
        return ClamdCommand

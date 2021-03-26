from icinga2confgen.Commands.NagiosPlugins.RadiusCommand import RadiusCommand
from tests.BaseCommandTest import BaseCommandTest


class TestRadiusCommand(BaseCommandTest):

    def get_instance_class(self):
        return RadiusCommand

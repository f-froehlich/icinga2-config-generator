from icinga2confgen.Commands.NagiosPlugins.SensorsCommand import SensorsCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSensorsCommand(BaseCommandTest):

    def get_instance_class(self):
        return SensorsCommand

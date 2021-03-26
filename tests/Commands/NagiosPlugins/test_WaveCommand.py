from icinga2confgen.Commands.NagiosPlugins.WaveCommand import WaveCommand
from tests.BaseCommandTest import BaseCommandTest


class TestWaveCommand(BaseCommandTest):

    def get_instance_class(self):
        return WaveCommand

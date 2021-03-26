from icinga2confgen.Commands.NagiosPlugins.MRTGtrafCommand import MRTGtrafCommand
from tests.BaseCommandTest import BaseCommandTest


class TestMRTGtrafCommand(BaseCommandTest):

    def get_instance_class(self):
        return MRTGtrafCommand

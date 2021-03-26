from icinga2confgen.Commands.NagiosPlugins.NNTPCommand import NNTPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestNNTPCommand(BaseCommandTest):

    def get_instance_class(self):
        return NNTPCommand

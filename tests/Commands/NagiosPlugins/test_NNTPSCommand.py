from icinga2confgen.Commands.NagiosPlugins.NNTPSCommand import NNTPSCommand
from tests.BaseCommandTest import BaseCommandTest


class TestNNTPSCommand(BaseCommandTest):

    def get_instance_class(self):
        return NNTPSCommand

from icinga2confgen.Commands.Other.SynologyStatusCommand import SynologyStatusCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSynologyStatusCommand(BaseCommandTest):

    def get_instance_class(self):
        return SynologyStatusCommand

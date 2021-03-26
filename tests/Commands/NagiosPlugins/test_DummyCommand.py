from icinga2confgen.Commands.NagiosPlugins.DummyCommand import DummyCommand
from tests.BaseCommandTest import BaseCommandTest


class TestDummyCommand(BaseCommandTest):

    def get_instance_class(self):
        return DummyCommand

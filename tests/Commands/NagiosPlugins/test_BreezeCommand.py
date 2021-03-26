from icinga2confgen.Commands.NagiosPlugins.BreezeCommand import BreezeCommand
from tests.BaseCommandTest import BaseCommandTest


class TestBreezeCommand(BaseCommandTest):

    def get_instance_class(self):
        return BreezeCommand

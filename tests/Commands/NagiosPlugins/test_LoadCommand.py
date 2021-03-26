from icinga2confgen.Commands.NagiosPlugins.LoadCommand import LoadCommand
from tests.BaseCommandTest import BaseCommandTest


class TestLoadCommand(BaseCommandTest):

    def get_instance_class(self):
        return LoadCommand

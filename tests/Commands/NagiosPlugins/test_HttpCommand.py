from icinga2confgen.Commands.NagiosPlugins.HttpCommand import HttpCommand
from tests.BaseCommandTest import BaseCommandTest


class TestHttpCommand(BaseCommandTest):

    def get_instance_class(self):
        return HttpCommand

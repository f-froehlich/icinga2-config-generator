from icinga2confgen.Commands.NagiosPlugins.DigCommand import DigCommand
from tests.BaseCommandTest import BaseCommandTest


class TestDigCommand(BaseCommandTest):

    def get_instance_class(self):
        return DigCommand

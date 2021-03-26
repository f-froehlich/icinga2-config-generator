from icinga2confgen.Commands.ClaudioKuenzler.StorcenterCommand import StorcenterCommand
from tests.BaseCommandTest import BaseCommandTest


class TestStorcenterCommand(BaseCommandTest):

    def get_instance_class(self):
        return StorcenterCommand

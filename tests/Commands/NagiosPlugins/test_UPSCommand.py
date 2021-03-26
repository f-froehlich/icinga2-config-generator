from icinga2confgen.Commands.NagiosPlugins.UPSCommand import UPSCommand
from tests.BaseCommandTest import BaseCommandTest


class TestUPSCommand(BaseCommandTest):

    def get_instance_class(self):
        return UPSCommand

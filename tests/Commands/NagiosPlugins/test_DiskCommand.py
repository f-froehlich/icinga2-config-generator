from icinga2confgen.Commands.NagiosPlugins.DiskCommand import DiskCommand
from tests.BaseCommandTest import BaseCommandTest


class TestDiskCommand(BaseCommandTest):

    def get_instance_class(self):
        return DiskCommand

from icinga2confgen.Commands.NagiosPlugins.DiskSMBCommand import DiskSMBCommand
from tests.BaseCommandTest import BaseCommandTest


class TestDiskSMBCommand(BaseCommandTest):

    def get_instance_class(self):
        return DiskSMBCommand

from icinga2confgen.Commands.NagiosPlugins.IrcdCommand import IrcdCommand
from tests.BaseCommandTest import BaseCommandTest


class TestIrcdCommand(BaseCommandTest):

    def get_instance_class(self):
        return IrcdCommand

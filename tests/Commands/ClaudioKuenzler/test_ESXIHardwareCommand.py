from icinga2confgen.Commands.ClaudioKuenzler.ESXIHardwareCommand import ESXIHardwareCommand
from tests.BaseCommandTest import BaseCommandTest


class TestESXIHardwareCommand(BaseCommandTest):

    def get_instance_class(self):
        return ESXIHardwareCommand

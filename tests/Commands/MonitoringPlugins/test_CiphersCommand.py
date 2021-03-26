from icinga2confgen.Commands.MonitoringPlugins.CiphersCommand import CiphersCommand
from tests.BaseCommandTest import BaseCommandTest


class TestCiphersCommand(BaseCommandTest):

    def get_instance_class(self):
        return CiphersCommand

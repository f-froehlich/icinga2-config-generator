from icinga2confgen.Commands.MonitoringPlugins.DenyTlsVersionCommand import DenyTlsVersionCommand
from tests.BaseCommandTest import BaseCommandTest


class TestDenyTlsVersionCommand(BaseCommandTest):

    def get_instance_class(self):
        return DenyTlsVersionCommand

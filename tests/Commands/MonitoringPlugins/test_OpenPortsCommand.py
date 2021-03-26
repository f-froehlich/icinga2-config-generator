from icinga2confgen.Commands.MonitoringPlugins.OpenPortsCommand import OpenPortsCommand
from tests.BaseCommandTest import BaseCommandTest


class TestOpenPortsCommand(BaseCommandTest):

    def get_instance_class(self):
        return OpenPortsCommand

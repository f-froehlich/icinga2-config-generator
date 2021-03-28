from icinga2confgen.Commands.MonitoringPlugins.OpenPortsCommand import OpenPortsCommand
from tests.BaseNMAPCommandTest import BaseNMAPCommandTest


class TestOpenPortsCommand(BaseNMAPCommandTest):

    def get_instance_class(self):
        return OpenPortsCommand

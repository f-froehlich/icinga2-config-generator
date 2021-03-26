from icinga2confgen.Commands.MonitoringPlugins.SPFCommand import SPFCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSPFCommand(BaseCommandTest):

    def get_instance_class(self):
        return SPFCommand

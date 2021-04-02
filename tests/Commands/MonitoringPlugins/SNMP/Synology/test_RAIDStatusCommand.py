from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.RAIDStatusCommand import RAIDStatusCommand
from tests.BaseCommandTest import BaseCommandTest


class TestRAIDStatusCommand(BaseCommandTest):

    def get_instance_class(self):
        return RAIDStatusCommand

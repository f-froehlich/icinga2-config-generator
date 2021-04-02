from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.SpaceIOCommand import SpaceIOCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSpaceIOCommand(BaseCommandTest):

    def get_instance_class(self):
        return SpaceIOCommand

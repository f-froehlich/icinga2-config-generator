from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.SystemStatusCommand import SystemStatusCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSystemStatusCommand(BaseCommandTest):

    def get_instance_class(self):
        return SystemStatusCommand

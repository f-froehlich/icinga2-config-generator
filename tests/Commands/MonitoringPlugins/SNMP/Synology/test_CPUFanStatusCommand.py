from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.CPUFanStatusCommand import CPUFanStatusCommand
from tests.BaseCommandTest import BaseCommandTest


class TestCPUFanStatusCommand(BaseCommandTest):

    def get_instance_class(self):
        return CPUFanStatusCommand

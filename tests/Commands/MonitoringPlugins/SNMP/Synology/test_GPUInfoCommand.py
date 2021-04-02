from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.GPUInfoCommand import GPUInfoCommand
from tests.BaseCommandTest import BaseCommandTest


class TestGPUInfoCommand(BaseCommandTest):

    def get_instance_class(self):
        return GPUInfoCommand

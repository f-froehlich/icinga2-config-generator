from icinga2confgen.Commands.MonitoringPlugins.SNMP.UCD_SNMP_MIB.MemoryCommand import MemoryCommand
from tests.BaseCommandTest import BaseCommandTest


class TestMemoryCommand(BaseCommandTest):

    def get_instance_class(self):
        return MemoryCommand

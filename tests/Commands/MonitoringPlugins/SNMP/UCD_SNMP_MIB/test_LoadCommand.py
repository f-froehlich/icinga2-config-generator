from icinga2confgen.Commands.MonitoringPlugins.SNMP.UCD_SNMP_MIB.LoadCommand import LoadCommand
from tests.BaseCommandTest import BaseCommandTest


class TestLoadCommand(BaseCommandTest):

    def get_instance_class(self):
        return LoadCommand

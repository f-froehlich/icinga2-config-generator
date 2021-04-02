from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.SMARTCommand import SMARTCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSMARTCommand(BaseCommandTest):

    def get_instance_class(self):
        return SMARTCommand

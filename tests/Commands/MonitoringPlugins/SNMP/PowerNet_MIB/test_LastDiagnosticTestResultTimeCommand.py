from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.LastDiagnosticTestResultTimeCommand import \
    LastDiagnosticTestResultTimeCommand
from tests.BaseCommandTest import BaseCommandTest


class TestLastDiagnosticTestResultTimeCommand(BaseCommandTest):

    def get_instance_class(self):
        return LastDiagnosticTestResultTimeCommand

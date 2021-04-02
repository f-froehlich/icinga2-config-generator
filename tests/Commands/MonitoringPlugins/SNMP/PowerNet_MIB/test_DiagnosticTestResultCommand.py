from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.DiagnosticTestResultCommand import \
    DiagnosticTestResultCommand
from tests.BaseCommandTest import BaseCommandTest


class TestDiagnosticTestResultCommand(BaseCommandTest):

    def get_instance_class(self):
        return DiagnosticTestResultCommand

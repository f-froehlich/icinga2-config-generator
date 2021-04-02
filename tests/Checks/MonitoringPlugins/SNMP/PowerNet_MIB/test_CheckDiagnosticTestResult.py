from icinga2confgen.Checks.MonitoringPlugins.SNMP.PowerNet_MIB.CheckDiagnosticTestResult import \
    CheckDiagnosticTestResult
from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.DiagnosticTestResultCommand import \
    DiagnosticTestResultCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckDiagnosticTestResult(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckDiagnosticTestResult

    def get_command_class(self):
        return DiagnosticTestResultCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ups'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

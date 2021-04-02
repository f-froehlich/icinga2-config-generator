from icinga2confgen.Checks.MonitoringPlugins.SNMP.PowerNet_MIB.CheckLastDiagnosticTestResultTime import \
    CheckLastDiagnosticTestResultTime
from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.LastDiagnosticTestResultTimeCommand import \
    LastDiagnosticTestResultTimeCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckLastDiagnosticTestResultTime(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckLastDiagnosticTestResultTime

    def get_command_class(self):
        return LastDiagnosticTestResultTimeCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ups'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

    def test_get_right_warning(self):
        instance = self.create_instance()
        instance.set_warning(44)

        assert 44 == instance.get_warning()

    def test_get_right_critical(self):
        instance = self.create_instance()
        instance.set_critical(44)

        assert 44 == instance.get_critical()

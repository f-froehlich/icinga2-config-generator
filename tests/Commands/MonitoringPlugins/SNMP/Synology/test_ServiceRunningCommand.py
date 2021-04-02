from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.ServiceRunningCommand import ServiceRunningCommand
from tests.BaseCommandTest import BaseCommandTest


class TestServiceRunningCommand(BaseCommandTest):

    def get_instance_class(self):
        return ServiceRunningCommand

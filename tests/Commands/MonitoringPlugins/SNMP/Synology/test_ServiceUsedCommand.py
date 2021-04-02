from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.ServiceUsedCommand import ServiceUsedCommand
from tests.BaseCommandTest import BaseCommandTest


class TestServiceUsedCommand(BaseCommandTest):

    def get_instance_class(self):
        return ServiceUsedCommand

from icinga2confgen.Commands.MonitoringPlugins.DNSSECExpireCommand import DNSSECExpireCommand
from tests.BaseCommandTest import BaseCommandTest


class TestDNSSECExpireCommand(BaseCommandTest):

    def get_instance_class(self):
        return DNSSECExpireCommand

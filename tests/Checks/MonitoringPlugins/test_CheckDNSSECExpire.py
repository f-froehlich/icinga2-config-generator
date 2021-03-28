from icinga2confgen.Checks.MonitoringPlugins.CheckDNSSECExpire import CheckDNSSECExpire
from icinga2confgen.Commands.MonitoringPlugins.DNSSECExpireCommand import DNSSECExpireCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckDNSSECExpire(BaseCheckTest):

    def get_instance_class(self):
        return CheckDNSSECExpire

    def get_command_class(self):
        return DNSSECExpireCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('dns'),
            ServiceGroup.create('dnssec'),
            ServiceGroup.create('security'),
        ]

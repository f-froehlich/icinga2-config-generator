from icinga2confgen.Checks.MonitoringPlugins.CheckUFWStatus import CheckUFWStatus
from icinga2confgen.Commands.MonitoringPlugins.UFWStatusCommand import UFWStatusCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckUFWStatus(BaseCheckTest):

    def get_instance_class(self):
        return CheckUFWStatus

    def get_command_class(self):
        return UFWStatusCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ufw'),
            ServiceGroup.create('security'),
            ServiceGroup.create('firewall')
        ]

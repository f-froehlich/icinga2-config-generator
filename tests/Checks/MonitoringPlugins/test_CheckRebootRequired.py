from icinga2confgen.Checks.MonitoringPlugins.CheckRebootRequired import CheckRebootRequired
from icinga2confgen.Commands.MonitoringPlugins.RebootRequiredCommand import RebootRequiredCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckRebootRequired(BaseCheckTest):

    def get_instance_class(self):
        return CheckRebootRequired

    def get_command_class(self):
        return RebootRequiredCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('system_health'),
            ServiceGroup.create('reboot'),
        ]

from icinga2confgen.Checks.NagiosPlugins.CheckUptime import CheckUptime
from icinga2confgen.Commands.NagiosPlugins.UptimeCommand import UptimeCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckUptime(BaseCheckTest):

    def get_instance_class(self):
        return CheckUptime

    def get_command_class(self):
        return UptimeCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('uptime'),
            ServiceGroup.create('system_health')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_warning('10')
        instance.set_critical('20')
        return instance

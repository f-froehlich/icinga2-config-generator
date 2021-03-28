from icinga2confgen.Checks.NagiosPlugins.CheckApt import CheckApt
from icinga2confgen.Commands.NagiosPlugins.AptCommand import AptCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckApt(BaseCheckTest):

    def get_instance_class(self):
        return CheckApt

    def get_command_class(self):
        return AptCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('apt'),
            ServiceGroup.create('updates'),
        ]

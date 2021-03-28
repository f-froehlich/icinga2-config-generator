from icinga2confgen.Checks.NagiosPlugins.CheckIdeSmart import CheckIdeSmart
from icinga2confgen.Commands.NagiosPlugins.IdeSmartCommand import IdeSmartCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckIdeSmart(BaseCheckTest):

    def get_instance_class(self):
        return CheckIdeSmart

    def get_command_class(self):
        return IdeSmartCommand

    def get_default_check_interval(self) -> str:
        return '24h'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('smart'),
            ServiceGroup.create('disk'),
        ]

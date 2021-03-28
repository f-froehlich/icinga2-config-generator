from icinga2confgen.Checks.NagiosPlugins.CheckDummy import CheckDummy
from icinga2confgen.Commands.NagiosPlugins.DummyCommand import DummyCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckDummy(BaseCheckTest):

    def get_instance_class(self):
        return CheckDummy

    def get_command_class(self):
        return DummyCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('dummy'),
        ]

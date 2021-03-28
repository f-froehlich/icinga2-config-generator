from icinga2confgen.Checks.NagiosPlugins.CheckDig import CheckDig
from icinga2confgen.Commands.NagiosPlugins.DigCommand import DigCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckDig(BaseCheckTest):

    def get_instance_class(self):
        return CheckDig

    def get_command_class(self):
        return DigCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('dig'),
            ServiceGroup.create('dns'),
            ServiceGroup.create('network'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_question('question')
        instance.set_expected_address('address')
        return instance

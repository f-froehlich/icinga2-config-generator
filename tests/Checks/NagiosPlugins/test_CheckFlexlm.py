from icinga2confgen.Checks.NagiosPlugins.CheckFlexlm import CheckFlexlm
from icinga2confgen.Commands.NagiosPlugins.FlexlmCommand import FlexlmCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckFlexlm(BaseCheckTest):

    def get_instance_class(self):
        return CheckFlexlm

    def get_command_class(self):
        return FlexlmCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('flexlm'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_file('file')
        return instance

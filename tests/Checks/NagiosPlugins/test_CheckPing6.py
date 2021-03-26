from icinga2confgen.Checks.NagiosPlugins.CheckPing6 import CheckPing6
from icinga2confgen.Commands.NagiosPlugins.PingCommand import PingCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckPing6(BaseCheckTest):

    def get_instance_class(self):
        return CheckPing6

    def get_command_class(self):
        return PingCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ping'),
            ServiceGroup.create('network')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_address('address')
        return instance

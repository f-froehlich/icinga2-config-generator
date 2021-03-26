from icinga2confgen.Checks.NagiosPlugins.CheckRPC import CheckRPC
from icinga2confgen.Commands.NagiosPlugins.RPCCommand import RPCCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckRPC(BaseCheckTest):

    def get_instance_class(self):
        return CheckRPC

    def get_command_class(self):
        return RPCCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('rpc'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_command('command')
        return instance

from icinga2confgen.Checks.NagiosPlugins.CheckSPOP import CheckSPOP
from icinga2confgen.Commands.NagiosPlugins.SPOPCommand import SPOPCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckSPOP(BaseCheckTest):

    def get_instance_class(self):
        return CheckSPOP

    def get_command_class(self):
        return SPOPCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('mail'),
            ServiceGroup.create('pop'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_port(8888)
        return instance

from icinga2confgen.Checks.NagiosPlugins.CheckPOP import CheckPOP
from icinga2confgen.Commands.NagiosPlugins.POPCommand import POPCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckPOP(BaseCheckTest):

    def get_instance_class(self):
        return CheckPOP

    def get_command_class(self):
        return POPCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('pop'),
            ServiceGroup.create('mail'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_port(8888)
        return instance

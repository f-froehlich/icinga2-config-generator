from icinga2confgen.Checks.NagiosPlugins.CheckTCP import CheckTCP
from icinga2confgen.Commands.NagiosPlugins.TCPCommand import TCPCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckTCP(BaseCheckTest):

    def get_instance_class(self):
        return CheckTCP

    def get_command_class(self):
        return TCPCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('tcp'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_port(8888)
        return instance

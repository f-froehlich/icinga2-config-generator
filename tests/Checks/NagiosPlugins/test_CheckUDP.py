from icinga2confgen.Checks.NagiosPlugins.CheckUDP import CheckUDP
from icinga2confgen.Commands.NagiosPlugins.UDPCommand import UDPCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckUDP(BaseCheckTest):

    def get_instance_class(self):
        return CheckUDP

    def get_command_class(self):
        return UDPCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('udp'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_port(8888)
        return instance

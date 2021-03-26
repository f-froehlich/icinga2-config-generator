from icinga2confgen.Checks.NagiosPlugins.CheckICMP import CheckICMP
from icinga2confgen.Commands.NagiosPlugins.ICMPCommand import ICMPCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckICMP(BaseCheckTest):

    def get_instance_class(self):
        return CheckICMP

    def get_command_class(self):
        return ICMPCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('icmp'),
            ServiceGroup.create('network'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        return instance

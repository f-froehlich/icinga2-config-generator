from icinga2confgen.Checks.NagiosPlugins.CheckUPS import CheckUPS
from icinga2confgen.Commands.NagiosPlugins.UPSCommand import UPSCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckUPS(BaseCheckTest):

    def get_instance_class(self):
        return CheckUPS

    def get_command_class(self):
        return UPSCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ups'),
            ServiceGroup.create('system_health')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_ups('ups')
        return instance

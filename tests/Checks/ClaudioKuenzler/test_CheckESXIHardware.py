from icinga2confgen.Checks.ClaudioKuenzler.CheckESXIHardware import CheckESXIHardware
from icinga2confgen.Commands.ClaudioKuenzler.ESXIHardwareCommand import ESXIHardwareCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckESXIHardware(BaseCheckTest):

    def get_instance_class(self):
        return CheckESXIHardware

    def get_command_class(self):
        return ESXIHardwareCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('esxi_hardware'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_user('user')
        instance.set_password('password')
        return instance

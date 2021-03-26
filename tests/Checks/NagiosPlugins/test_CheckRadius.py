from icinga2confgen.Checks.NagiosPlugins.CheckRadius import CheckRadius
from icinga2confgen.Commands.NagiosPlugins.RadiusCommand import RadiusCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckRadius(BaseCheckTest):

    def get_instance_class(self):
        return CheckRadius

    def get_command_class(self):
        return RadiusCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('radius'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_config_file('config_file')
        instance.set_username('username')
        instance.set_password('password')
        return instance

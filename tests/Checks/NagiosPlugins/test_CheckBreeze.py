from icinga2confgen.Checks.NagiosPlugins.CheckBreeze import CheckBreeze
from icinga2confgen.Commands.NagiosPlugins.BreezeCommand import BreezeCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckBreeze(BaseCheckTest):

    def get_instance_class(self):
        return CheckBreeze

    def get_command_class(self):
        return BreezeCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('breeze'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_warning('30')
        instance.set_critical('40')
        return instance

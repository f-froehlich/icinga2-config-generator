from icinga2confgen.Checks.NagiosPlugins.CheckWave import CheckWave
from icinga2confgen.Commands.NagiosPlugins.WaveCommand import WaveCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckWave(BaseCheckTest):

    def get_instance_class(self):
        return CheckWave

    def get_command_class(self):
        return WaveCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('wave')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        return instance

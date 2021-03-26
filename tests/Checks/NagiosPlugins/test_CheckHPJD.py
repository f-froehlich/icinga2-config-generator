from icinga2confgen.Checks.NagiosPlugins.CheckHPJD import CheckHPJD
from icinga2confgen.Commands.NagiosPlugins.HPJDCommand import HPJDCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckHPJD(BaseCheckTest):

    def get_instance_class(self):
        return CheckHPJD

    def get_command_class(self):
        return HPJDCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('hpjd'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        return instance

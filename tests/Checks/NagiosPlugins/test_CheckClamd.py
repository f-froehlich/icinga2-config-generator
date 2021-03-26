from icinga2confgen.Checks.NagiosPlugins.CheckClamd import CheckClamd
from icinga2confgen.Commands.NagiosPlugins.ClamdCommand import ClamdCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckClamd(BaseCheckTest):

    def get_instance_class(self):
        return CheckClamd

    def get_command_class(self):
        return ClamdCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('clamd'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_port(8888)
        return instance

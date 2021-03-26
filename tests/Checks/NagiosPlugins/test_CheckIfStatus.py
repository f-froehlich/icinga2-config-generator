from icinga2confgen.Checks.NagiosPlugins.CheckIfStatus import CheckIfStatus
from icinga2confgen.Commands.NagiosPlugins.IfStatusCommand import IfStatusCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckIfStatus(BaseCheckTest):

    def get_instance_class(self):
        return CheckIfStatus

    def get_command_class(self):
        return IfStatusCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ifstatus'),
            ServiceGroup.create('network'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_community('community')
        return instance

from icinga2confgen.Checks.Other.CheckSynologyStatus import CheckSynologyStatus
from icinga2confgen.Commands.Other.SynologyStatusCommand import SynologyStatusCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckSynologyStatus(BaseCheckTest):

    def get_instance_class(self):
        return CheckSynologyStatus

    def get_command_class(self):
        return SynologyStatusCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('synology')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_user('user')
        instance.set_password('pwd')
        return instance

from icinga2confgen.Checks.ClaudioKuenzler.CheckStorcenter import CheckStorcenter
from icinga2confgen.Commands.ClaudioKuenzler.StorcenterCommand import StorcenterCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckStorcenter(BaseCheckTest):

    def get_instance_class(self):
        return CheckStorcenter

    def get_command_class(self):
        return StorcenterCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('storcenter'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_user('user')
        instance.set_password('password')
        instance.set_type('disk')
        return instance

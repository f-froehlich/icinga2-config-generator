from icinga2confgen.Checks.NagiosPlugins.CheckLDAPS import CheckLDAPS
from icinga2confgen.Commands.NagiosPlugins.LDAPSCommand import LDAPSCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckLDAPS(BaseCheckTest):

    def get_instance_class(self):
        return CheckLDAPS

    def get_command_class(self):
        return LDAPSCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ldap'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_base('base')
        return instance

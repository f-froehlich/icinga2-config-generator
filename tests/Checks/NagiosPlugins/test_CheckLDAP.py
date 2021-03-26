from icinga2confgen.Checks.NagiosPlugins.CheckLDAP import CheckLDAP
from icinga2confgen.Commands.NagiosPlugins.LDAPCommand import LDAPCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckLDAP(BaseCheckTest):

    def get_instance_class(self):
        return CheckLDAP

    def get_command_class(self):
        return LDAPCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ldap'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_base('base')
        return instance

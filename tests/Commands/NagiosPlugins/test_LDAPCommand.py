from icinga2confgen.Commands.NagiosPlugins.LDAPCommand import LDAPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestLDAPCommand(BaseCommandTest):

    def get_instance_class(self):
        return LDAPCommand

from icinga2confgen.Commands.NagiosPlugins.LDAPSCommand import LDAPSCommand
from tests.BaseCommandTest import BaseCommandTest


class TestLDAPSCommand(BaseCommandTest):

    def get_instance_class(self):
        return LDAPSCommand

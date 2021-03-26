from icinga2confgen.Commands.NagiosPlugins.MySQLQueryCommand import MySQLQueryCommand
from tests.BaseCommandTest import BaseCommandTest


class TestMySQLQueryCommand(BaseCommandTest):

    def get_instance_class(self):
        return MySQLQueryCommand

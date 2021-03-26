from icinga2confgen.Commands.NagiosPlugins.MySQLCommand import MySQLCommand
from tests.BaseCommandTest import BaseCommandTest


class TestMySQLCommand(BaseCommandTest):

    def get_instance_class(self):
        return MySQLCommand

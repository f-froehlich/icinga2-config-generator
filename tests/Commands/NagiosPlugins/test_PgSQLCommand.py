from icinga2confgen.Commands.NagiosPlugins.PgSQLCommand import PgSQLCommand
from tests.BaseCommandTest import BaseCommandTest


class TestPgSQLCommand(BaseCommandTest):

    def get_instance_class(self):
        return PgSQLCommand

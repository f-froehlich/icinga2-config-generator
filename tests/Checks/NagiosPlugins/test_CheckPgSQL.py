from icinga2confgen.Checks.NagiosPlugins.CheckPgSQL import CheckPgSQL
from icinga2confgen.Commands.NagiosPlugins.PgSQLCommand import PgSQLCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckPgSQL(BaseCheckTest):

    def get_instance_class(self):
        return CheckPgSQL

    def get_command_class(self):
        return PgSQLCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('postgres'),
            ServiceGroup.create('database'),
        ]

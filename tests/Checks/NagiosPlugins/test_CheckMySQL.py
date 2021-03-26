from icinga2confgen.Checks.NagiosPlugins.CheckMySQL import CheckMySQL
from icinga2confgen.Commands.NagiosPlugins.MySQLCommand import MySQLCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckMySQL(BaseCheckTest):

    def get_instance_class(self):
        return CheckMySQL

    def get_command_class(self):
        return MySQLCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('database'),
            ServiceGroup.create('mysql'),
        ]

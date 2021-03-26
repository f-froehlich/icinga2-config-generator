from icinga2confgen.Checks.NagiosPlugins.CheckMySQLQuery import CheckMySQLQuery
from icinga2confgen.Commands.NagiosPlugins.MySQLQueryCommand import MySQLQueryCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckMySQLQuery(BaseCheckTest):

    def get_instance_class(self):
        return CheckMySQLQuery

    def get_command_class(self):
        return MySQLQueryCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('database'),
            ServiceGroup.create('mysql'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_query('query')
        return instance

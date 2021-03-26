from icinga2confgen.Checks.NagiosPlugins.CheckLog import CheckLog
from icinga2confgen.Commands.NagiosPlugins.LogCommand import LogCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckLog(BaseCheckTest):

    def get_instance_class(self):
        return CheckLog

    def get_command_class(self):
        return LogCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('log'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_file('file')
        instance.set_oldfile('oldfile')
        instance.set_query('query')
        return instance

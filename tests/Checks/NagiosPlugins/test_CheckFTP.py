from icinga2confgen.Checks.NagiosPlugins.CheckFTP import CheckFTP
from icinga2confgen.Commands.NagiosPlugins.FTPCommand import FTPCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckFTP(BaseCheckTest):

    def get_instance_class(self):
        return CheckFTP

    def get_command_class(self):
        return FTPCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ftp'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        return instance

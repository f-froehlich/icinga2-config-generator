from icinga2confgen.Checks.NagiosPlugins.CheckIMAP import CheckIMAP
from icinga2confgen.Commands.NagiosPlugins.IMAPCommand import IMAPCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckIMAP(BaseCheckTest):

    def get_instance_class(self):
        return CheckIMAP

    def get_command_class(self):
        return IMAPCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('imap'),
            ServiceGroup.create('mail'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_port(8888)
        return instance

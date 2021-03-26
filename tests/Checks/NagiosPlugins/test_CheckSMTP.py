from icinga2confgen.Checks.NagiosPlugins.CheckSMTP import CheckSMTP
from icinga2confgen.Commands.NagiosPlugins.SMTPCommand import SMTPCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckSMTP(BaseCheckTest):

    def get_instance_class(self):
        return CheckSMTP

    def get_command_class(self):
        return SMTPCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('smtp'),
            ServiceGroup.create('mail'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        return instance

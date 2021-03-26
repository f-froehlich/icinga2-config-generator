from icinga2confgen.Checks.NagiosPlugins.CheckSSMTP import CheckSSMTP
from icinga2confgen.Commands.NagiosPlugins.SSMTPCommand import SSMTPCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckSSMTP(BaseCheckTest):

    def get_instance_class(self):
        return CheckSSMTP

    def get_command_class(self):
        return SSMTPCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('mail'),
            ServiceGroup.create('smtp'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_port(8888)
        return instance

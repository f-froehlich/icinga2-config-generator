from icinga2confgen.Checks.NagiosPlugins.CheckMailq import CheckMailq
from icinga2confgen.Commands.NagiosPlugins.MailqCommand import MailqCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckMailq(BaseCheckTest):

    def get_instance_class(self):
        return CheckMailq

    def get_command_class(self):
        return MailqCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('mailq'),
            ServiceGroup.create('mail')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_warning(30)
        instance.set_critical(40)
        return instance

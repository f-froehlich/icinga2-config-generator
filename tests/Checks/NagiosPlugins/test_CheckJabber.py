from icinga2confgen.Checks.NagiosPlugins.CheckJabber import CheckJabber
from icinga2confgen.Commands.NagiosPlugins.JabberCommand import JabberCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckJabber(BaseCheckTest):

    def get_instance_class(self):
        return CheckJabber

    def get_command_class(self):
        return JabberCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('jabber'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_port(8888)
        return instance

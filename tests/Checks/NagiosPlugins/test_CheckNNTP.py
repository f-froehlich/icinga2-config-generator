from icinga2confgen.Checks.NagiosPlugins.CheckNNTP import CheckNNTP
from icinga2confgen.Commands.NagiosPlugins.NNTPCommand import NNTPCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckNNTP(BaseCheckTest):

    def get_instance_class(self):
        return CheckNNTP

    def get_command_class(self):
        return NNTPCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('nntp'),
            ServiceGroup.create('network'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_port(8888)
        return instance

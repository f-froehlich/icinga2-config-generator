from icinga2confgen.Checks.NagiosPlugins.CheckNT import CheckNT
from icinga2confgen.Commands.NagiosPlugins.NTCommand import NTCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckNT(BaseCheckTest):

    def get_instance_class(self):
        return CheckNT

    def get_command_class(self):
        return NTCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ns_client'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_variable('variable')
        return instance

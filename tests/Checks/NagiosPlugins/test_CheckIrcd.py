from icinga2confgen.Checks.NagiosPlugins.CheckIrcd import CheckIrcd
from icinga2confgen.Commands.NagiosPlugins.IrcdCommand import IrcdCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckIrcd(BaseCheckTest):

    def get_instance_class(self):
        return CheckIrcd

    def get_command_class(self):
        return IrcdCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ircd'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        return instance
